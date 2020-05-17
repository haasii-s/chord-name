import React from "react";

import { OutputChord } from "../../utils/service";

import Keys from "./Keys";

interface Props {
  chord: OutputChord;
}

const Piano: React.FC<Props> = ({ chord }) => {
  return <Keys chord={chord} />;
};

export default Piano;
