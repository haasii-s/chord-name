import { Chord, chordQualities } from "./chordQualities";

import { intervals, suspensions, extensions, Interval } from "./intervals";
import { flatRoots, sharpRoots } from "./rootNotes";

export interface OutputChord {
  root?: string;
  quality?: Chord;
  suspension?: Interval;
  extension?: Interval;
  semitones?: number[];
  notes?: string[];
}

const numFrom = (str: string) => str.replace(/\D/g, "");

const findRoot: (chord: string) => string | undefined = chord => {
  const firstTwoLetters = chord.substr(0, 2);
  const firstLetter = chord.substr(0, 1);

  const hasRoot = (str: string) =>
    sharpRoots.includes(str) || flatRoots.includes(str);

  return (
    (hasRoot(firstTwoLetters) && firstTwoLetters) ||
    (hasRoot(firstLetter) && firstLetter) ||
    undefined
  );
};

const findQuality: (modifiers: string) => Chord | undefined = modifiers => {
  const mapQual = chordQualities.map(quality =>
    modifiers.includes(quality.name) ? quality : undefined
  );
  const filterQual = mapQual.filter(quality => quality);
  const quality = filterQual.length ? filterQual[0] : undefined;

  return quality;
};

const findModifiers: (
  arr: Interval[],
  modifiers: string
) => Interval | undefined = (arr, modifiers) => {
  const mapMod = arr.map(mod =>
    modifiers.includes(mod.int) ? mod : undefined
  );
  const filterMod = mapMod.filter(mod => mod);
  const modifier = filterMod.length ? filterMod[0] : undefined;

  return modifier;
};

const applySus: (intervals: string[], suspension?: Interval) => string[] = (
  intervals,
  suspension
) =>
  intervals.map(interval => {
    if (!suspension) return interval;
    if (suspension.int === "sus2" && numFrom(interval) === "3") return "2";
    if (suspension.int === "sus4" && numFrom(interval) === "3") return "4";
    return interval;
  });

const applyExt: (intervals: string[], extension?: Interval) => string[] = (
  intervals,
  extension
) =>
  intervals.map(interval => {
    if (!extension) return interval;
    if (numFrom(extension.int) === numFrom(interval)) return extension.int;
    return interval;
  });

const modify: (
  quality: Chord,
  suspension: Interval | undefined,
  extension: Interval | undefined
) => string[] = (quality, suspension, extension) => {
  const suspendedIntervals = applySus(quality.intervals, suspension);
  const extendedIntervals = applyExt(suspendedIntervals, extension);

  return extendedIntervals;
};

const getSemitones: (intervals: string[]) => number[] = modifiedIntervals => {
  const semitones = modifiedIntervals.map(int => {
    const selectIdx = intervals.map(interval => interval.int).indexOf(int);
    if (selectIdx < 0) return 0;
    const semitone = intervals[selectIdx].sTones;
    return semitone;
  });
  return semitones;
};

const getNotes: (root: string, semitones: number[]) => string[] = (
  root,
  semitones
) => {
  const rootsArr = flatRoots.includes(root) ? flatRoots : sharpRoots;
  const rootIdx = rootsArr.indexOf(root);

  const intervalNotes = semitones.map(semitone => {
    const idx = rootIdx + semitone;
    return rootsArr[idx < 12 ? idx : idx - 12];
  });

  const chordNotes = [root, ...intervalNotes];
  const notes = chordNotes.filter((v, i, a) => a.indexOf(v) === i); // unique values
  return notes;
};

export const getChord: (chord: string) => OutputChord = chord => {
  if (chord && chord.length) {
    const root = findRoot(chord);

    if (!root) return {};

    const modifiers = chord.substr(root.length, chord.length);

    const quality = findQuality(modifiers);
    const suspension = findModifiers(suspensions, modifiers);
    const extension = findModifiers(extensions, modifiers);

    if (!quality) return { root };

    const modifiedIntervals = modify(quality, suspension, extension);
    const semitonesFromIntervals = getSemitones(modifiedIntervals);
    const notes = getNotes(root, semitonesFromIntervals);

    const semitones = [0, ...semitonesFromIntervals];

    return { root, quality, suspension, extension, semitones, notes };
  }
  return {};
};
