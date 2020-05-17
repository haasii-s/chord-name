import React from "react";

import { OutputChord } from "../utils/service";

import Divider from "antd/lib/divider";
import Typography from "antd/lib/typography";

const { Text } = Typography;

interface Props {
  input: string;
  chord: OutputChord;
}

const Calculator: React.FC<Props> = ({ input, chord }) => {
  const { root, quality, suspension, extension, semitones, notes } = chord;

  const fields = [
    {
      key: "output",
      label: "Output",
      condition: input.length > 0 && notes,
      output: `${root ? root + " " : ""}${quality ? quality.name + " " : ""}${
        suspension ? suspension.int + " " : ""
      }${extension ? extension.int : ""}`
    },
    {
      key: "root",
      label: "Root",
      condition: root,
      output: root
    },
    {
      key: "quality",
      label: "Quality",
      condition: quality,
      output: quality?.name !== "" ? quality?.name : "Root Triad"
    },
    {
      key: "suspension",
      label: "Suspension",
      condition: suspension,
      output: suspension?.int
    },
    {
      key: "extension",
      label: "Extension",
      condition: extension,
      output: extension?.int
    },
    {
      key: "semitones",
      label: "Semitones",
      condition: semitones,
      output: semitones?.join(", ")
    },
    {
      key: "notes",
      label: "Notes",
      condition: notes,
      output: notes?.join(", ")
    }
  ];

  return (
    <>
      <Divider />
      {fields.map((field, i) => {
        const { condition, key, label, output } = field;
        return (
          <React.Fragment key={key}>
            {condition && (
              <>
                <Text>
                  {label}: <Text code>{output}</Text>
                </Text>
                <Divider />
              </>
            )}
          </React.Fragment>
        );
      })}
    </>
  );
};

export default Calculator;
