import React from "react";

import { notes } from "./notes";

import BlackKey from "./BlackKey";
import WhiteKey from "./WhiteKey";

interface Props {
  index: number;
  isPressed: boolean;
  highlighted?: boolean;
  isLabelVisible?: boolean;
  isRoot?: boolean;
}

const Key: React.FC<Props> = ({
  index,
  isPressed,
  highlighted,
  isLabelVisible,
  isRoot
}) => {
  const note = notes.filter(note => note.index === index)[0];
  const { color, value, octave } = note;

  const label = isLabelVisible ? value[0] + octave.toString() : undefined;

  return (
    <>
      {color === "black" ? (
        <BlackKey
          label={label}
          isPressed={isPressed}
          highlighted={highlighted}
          isRoot={isRoot}
        />
      ) : (
        <WhiteKey
          label={label}
          isPressed={isPressed}
          highlighted={highlighted}
          isRoot={isRoot}
        />
      )}
    </>
  );
};

export default Key;
