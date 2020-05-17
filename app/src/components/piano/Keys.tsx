import React, { useState, useEffect } from "react";

import Soundfont from "soundfont-player";

import { OutputChord } from "../../utils/service";
import { Note, notes } from "./notes";

import Key from "./Key";

const { instrument } = Soundfont;

const range = {
  start: 51,
  end: 77
};

interface Props {
  chord: OutputChord;
}

const Keys: React.FC<Props> = ({ chord }) => {
  const [pressedNotes, setPressedNotes] = useState<number[]>([]);
  const [instr, setInstr] = useState<Soundfont.Player | undefined>(undefined);

  const availableKeys = notes.filter(
    note => note.index >= range.start && note.index <= range.end
  );
  const rootIdx = availableKeys.filter(
    key => key.value.indexOf(chord?.root!) > -1
  )[0]?.index;
  const shiftedChord = chord?.semitones?.map(semitone => semitone + rootIdx!);

  const callbackInstrument = async () => {
    const instr = await instrument(new AudioContext(), "acoustic_grand_piano");
    if (instr) setInstr(instr);
  };

  useEffect(() => {
    callbackInstrument();
  }, []);

  useEffect(() => {
    instr?.stop();
    if (shiftedChord)
      shiftedChord?.forEach(i => instr?.play(JSON.stringify(i)));
  }, [instr, shiftedChord]);

  const soundKey = (index: number) => instr?.play(JSON.stringify(index));

  return (
    <>
      {availableKeys.map((key: Note) => {
        const { index } = key;
        const isKeyInChord = shiftedChord?.includes(index);
        const isPressed = pressedNotes.includes(index);
        const isRoot = index === rootIdx;
        const isLabelVisible = index === range.start || index === range.end;

        const handlePress = () => {
          setPressedNotes([...pressedNotes, index]);
          soundKey(index);
        };

        const handleRelease = () =>
          setPressedNotes(pressedNotes.filter(i => i !== index));

        return (
          <div
            key={index}
            style={{ display: "inline-block" }}
            onMouseDown={handlePress}
            onMouseUp={handleRelease}
            onMouseOut={handleRelease}
          >
            <Key
              index={index}
              isPressed={isPressed}
              highlighted={isKeyInChord}
              isLabelVisible={isLabelVisible}
              isRoot={isRoot}
            />
          </div>
        );
      })}
    </>
  );
};

export default Keys;
