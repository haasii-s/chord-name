import React from "react";

import { variables } from "./variables";

interface Props {
  isPressed: boolean;
  label?: string;
  highlighted?: boolean;
  isRoot?: boolean;
}

const BlackKey: React.FC<Props> = ({
  isPressed,
  label,
  highlighted,
  isRoot
}) => {
  return (
    <div style={{ display: "inline-block", position: "relative" }}>
      {label && (
        <label
          style={{
            position: "absolute",
            width: variables.whiteKeyWidth,
            textAlign: "center",
            bottom: -30
          }}
        >
          {label}
        </label>
      )}
      <div
        style={{
          width: variables.blackKeyWidth,
          height: variables.blackKeyHeight + (highlighted ? 2 : 0),
          background: isRoot
            ? variables.color.highlight
            : highlighted
            ? variables.color.blackPressed
            : variables.color.black,

          position: "absolute",
          zIndex: 1,
          top: -variables.whiteKeyHeight - 1,
          left: -variables.blackKeyWidth / 2,
          border: isPressed ? `4px solid red` : `none`
        }}
      >
        {highlighted && (
          <div
            style={{
              transition: "all 0.2s ease",
              zIndex: 2,
              position: "absolute",
              borderRadius: variables.blackKeyWidth,
              width: variables.blackKeyWidth / 2,
              height: variables.blackKeyWidth / 2,
              bottom: 8,
              left: variables.blackKeyWidth / 4,
              background: variables.color.highlight
            }}
          />
        )}
      </div>
    </div>
  );
};

export default BlackKey;
