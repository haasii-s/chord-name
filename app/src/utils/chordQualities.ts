export interface Chord {
  name: string;
  intervals: string[];
}

export const chordQualities: Chord[] = [
  { name: "maj13", intervals: ["3", "5", "7", "9", "11", "13"] },
  { name: "maj11", intervals: ["3", "5", "7", "9", "11"] },
  { name: "maj9", intervals: ["3", "5", "7", "9"] },
  { name: "maj7", intervals: ["3", "5", "7"] },
  { name: "maj6", intervals: ["3", "5", "6"] },
  { name: "maj", intervals: ["3", "5"] },

  { name: "min7b5", intervals: ["b3", "b5", "b7"] },
  { name: "m7b5", intervals: ["b3", "b5", "b7"] },

  { name: "minMaj13", intervals: ["b3", "5", "7", "9", "11", "13"] },
  { name: "minMaj11", intervals: ["b3", "5", "7", "9", "11"] },
  { name: "minMaj9", intervals: ["b3", "5", "7", "9"] },
  { name: "minMaj7", intervals: ["b3", "5", "7"] },

  { name: "mMaj13", intervals: ["b3", "5", "7", "9", "11", "13"] },
  { name: "mMaj11", intervals: ["b3", "5", "7", "9", "11"] },
  { name: "mMaj9", intervals: ["b3", "5", "7", "9"] },
  { name: "mMaj7", intervals: ["b3", "5", "7"] },

  { name: "min13", intervals: ["b3", "5", "b7", "9", "11", "13"] },
  { name: "min11", intervals: ["b3", "5", "b7", "9", "11"] },
  { name: "min9", intervals: ["b3", "5", "b7", "9"] },
  { name: "min6/9", intervals: ["b3", "5", "6", "9"] },
  { name: "min7", intervals: ["b3", "5", "b7"] },
  { name: "min6", intervals: ["b3", "5", "6"] },
  { name: "min", intervals: ["b3", "5"] },

  { name: "dom13", intervals: ["3", "5", "b7", "9", "11", "13"] },
  { name: "dom11", intervals: ["3", "5", "b7", "9", "11"] },
  { name: "dom9", intervals: ["3", "5", "b7", "9"] },
  { name: "dom7", intervals: ["3", "5", "b7"] },

  { name: "dim13", intervals: ["b3", "b5", "6", "9", "11", "13"] },
  { name: "dim11", intervals: ["b3", "b5", "6", "9", "11"] },
  { name: "dim9", intervals: ["b3", "b5", "6", "9"] },
  { name: "dim7", intervals: ["b3", "b5", "6"] },
  { name: "dim", intervals: ["b3", "b5"] },

  { name: "aug13", intervals: ["3", "#5", "7", "9", "11", "13"] },
  { name: "aug11", intervals: ["3", "#5", "7", "9", "11"] },
  { name: "aug9", intervals: ["3", "#5", "7", "9"] },
  { name: "aug7", intervals: ["3", "#5", "7"] },
  { name: "aug", intervals: ["3", "#5"] },

  { name: "M13", intervals: ["3", "5", "7", "9", "11", "13"] },
  { name: "M11", intervals: ["3", "5", "7", "9", "11"] },
  { name: "M9", intervals: ["3", "5", "7", "9"] },
  { name: "M6/9", intervals: ["3", "5", "6", "9"] },
  { name: "M7", intervals: ["3", "5", "7"] },
  { name: "M6", intervals: ["3", "5", "6"] },
  { name: "M", intervals: ["3", "5"] },

  { name: "m13", intervals: ["b3", "5", "b7", "9", "11", "13"] },
  { name: "m11", intervals: ["b3", "5", "b7", "9", "11"] },
  { name: "m9", intervals: ["b3", "5", "b7", "9"] },
  { name: "m6/9", intervals: ["b3", "5", "6", "9"] },
  { name: "m7", intervals: ["b3", "5", "b7"] },
  { name: "m6", intervals: ["b3", "5", "6"] },
  { name: "m", intervals: ["b3", "5"] },

  { name: "13", intervals: ["3", "5", "b7", "9", "11", "13"] },
  { name: "11", intervals: ["3", "5", "b7", "9", "11"] },
  { name: "9", intervals: ["3", "5", "b7", "9"] },
  { name: "7", intervals: ["3", "5", "b7"] },
  { name: "5", intervals: ["3", "5", "6"] },
  { name: "", intervals: ["3", "5"] }
];
