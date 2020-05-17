export interface Interval {
  int: string;
  sTones: number;
}

export const intervals: Interval[] = [
  { int: "b2", sTones: 1 },
  { int: "2", sTones: 2 },
  { int: "b3", sTones: 3 },
  { int: "3", sTones: 4 },
  { int: "4", sTones: 5 },
  { int: "b5", sTones: 6 },
  { int: "5", sTones: 7 },
  { int: "#5", sTones: 8 },
  { int: "6", sTones: 9 },
  { int: "b7", sTones: 10 },
  { int: "7", sTones: 11 },
  { int: "b9", sTones: 12 },
  { int: "#9", sTones: 14 },
  { int: "9", sTones: 13 },
  { int: "#11", sTones: 17 },
  { int: "11", sTones: 16 },
  { int: "b13", sTones: 19 },
  { int: "13", sTones: 20 }
];

export const extensions: Interval[] = [
  { int: "add9", sTones: 2 },
  { int: "add2", sTones: 2 },
  { int: "b5", sTones: 6 },
  { int: "#5", sTones: 8 },
  { int: "b9", sTones: 12 },
  { int: "#9", sTones: 14 },
  { int: "#11", sTones: 17 },
  { int: "b13", sTones: 19 }
];

export const suspensions: Interval[] = [
  { int: "sus2", sTones: 2 },
  { int: "sus4", sTones: 5 }
];
