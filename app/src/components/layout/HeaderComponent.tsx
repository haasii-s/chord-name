import React from "react";

import Layout from "antd/lib/layout";
import Typography from "antd/lib/typography";
import Row from "antd/lib/row";

const { Header } = Layout;
const { Text } = Typography;

const HeaderComponent = () => {
  return (
    <Header
      style={{ background: "#fafafa", borderBottom: "1px solid #ededed" }}
    >
      <Row justify="space-between">
        <Text strong>Numpy Chords</Text>
        <a target="blank" href="https://gitlab.com/jono.vu/numpy-chords">
          GitLab
        </a>
      </Row>
    </Header>
  );
};

export default HeaderComponent;
