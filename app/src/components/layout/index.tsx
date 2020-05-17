import React, { ReactNode } from "react";

import HeaderComponent from "./HeaderComponent";

import Layout from "antd/lib/layout";
import Space from "antd/lib/space";
import Row from "antd/lib/row";
import Col from "antd/lib/col";

const { Content } = Layout;

interface Props {
  children: ReactNode;
}

const LayoutComponent: React.FC<Props> = ({ children }) => {
  return (
    <Layout>
      <HeaderComponent />
      <Content style={{ background: "white", padding: 40 }}>
        <Row justify="center">
          <Col span={24}>
            <Space direction="vertical" size="small" style={{ width: "100%" }}>
              {children}
            </Space>
          </Col>
        </Row>
      </Content>
    </Layout>
  );
};

export default LayoutComponent;
