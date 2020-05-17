import React, { useState } from "react";

import axios from "axios";
import { OutputChord } from "../utils/service";
import KeyboardEventHandler from "react-keyboard-event-handler";

import LayoutComponent from "./layout/index";
import Piano from "./piano/Piano";
import Calculator from "./Calculator";

import { DeleteOutlined } from "@ant-design/icons";

import "./calculator.css";

import Typography from "antd/lib/typography";
import Input from "antd/lib/input";
import Button from "antd/lib/button";
import List from "antd/lib/list";
import Space from "antd/lib/space";
import Card from "antd/lib/card";
import Row from "antd/lib/row";
import Col from "antd/lib/col";

const { Item } = List;
const { Text } = Typography;

const Landing: React.FC = () => {
  const [arr, setArr] = useState<string[]>([]);

  const addChord = (e: any) => {
    const value = e.target.value;
    if (value.length > 0) setArr([...arr, value]);
  };

  const getChord = (input: string) => {
    axios
      .post(`http://127.0.0.1:5000/`, { input })
      .then(res => res.data)
      .catch(err => console.log(err));
  };

  const handleChordPress = array => {
    const newArr = array.filter((v, i) => i !== 0);
    setCurrentChord(getChord(array[0]));
    setArr(newArr);
  };

  const [currentChord, setCurrentChord] = useState<any>({});

  console.log(currentChord);

  return (
    <LayoutComponent>
      <Row justify="center" gutter={40}>
        <Col>
          <KeyboardEventHandler
            handleKeys={["Space"]}
            onKeyEvent={() => handleChordPress(arr)}
          />
          <Piano chord={currentChord} />
          <br />
          <br />
          <br />
          <Calculator chord={currentChord} input={arr[0] || ""} />
        </Col>
        <Col>
          <Space direction="vertical" style={{ width: "100%" }}>
            <Text>Add a single Chord:</Text>
            <Input
              size="large"
              type="text"
              allowClear
              onPressEnter={addChord}
            />
            <br />
            <Text>
              Multiple chords separated by
              <Text code>space</Text>
            </Text>
            <Input
              size="large"
              type="text"
              allowClear
              onPressEnter={(e: any) => setArr(e.target.value.split(/\s+/))}
            />
            <br />
            {arr.length > 0 && (
              <Card
                size="small"
                title="Queued Chords"
                extra={
                  <Button type="primary" onClick={() => handleChordPress(arr)}>
                    Play Chord
                  </Button>
                }
              >
                <List size="small">
                  {arr.map((chordName, i) => {
                    return (
                      <Item key={i + chordName}>
                        {chordName}
                        <Button
                          type="link"
                          onClick={() => setArr(arr.filter((v, j) => j !== i))}
                        >
                          <DeleteOutlined />
                        </Button>
                      </Item>
                    );
                  })}
                </List>
              </Card>
            )}
          </Space>
        </Col>
      </Row>
    </LayoutComponent>
  );
};

export default Landing;
