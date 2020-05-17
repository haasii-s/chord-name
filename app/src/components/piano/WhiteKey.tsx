import React from "react";

import { variables } from "./variables";

interface Props {
  isPressed: boolean;
  label?: string;
  highlighted?: boolean;
  isRoot?: boolean;
}

const WhiteKey: React.FC<Props> = ({
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
          width: variables.whiteKeyWidth,
          height: variables.whiteKeyHeight,
          display: "inline-block",
          background: isRoot
            ? variables.color.highlight
            : highlighted
            ? variables.color.whitePressed
            : variables.color.white,
          outline: `1px solid ${variables.color.grey}`,
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
              bottom: 15,
              left: 9,
              background: variables.color.highlight
            }}
          />
        )}
      </div>
    </div>
  );
};

export default WhiteKey;
