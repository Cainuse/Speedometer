import React, { Component } from "react";
import { Sankey, Tooltip } from "recharts";
import _ from "lodash";
import SankeyLink from "./SankeyLink";
import SankeyNode from "./SankeyNode";

const data1 = {
  nodes: [
    { name: "Full Program" },
    { name: "Class 1" },
    { name: "Class 2" },
    { name: "bar1()" },
    { name: "bar2()" },
    { name: "foo1()" },
    { name: "foo2()" },
    { name: "foo3()" },
  ],
  links: [
    { source: 0, target: 1, value: 40 },
    { source: 0, target: 2, value: 60 },
    { source: 1, target: 3, value: 50 },
    { source: 1, target: 4, value: 50 },
    { source: 2, target: 5, value: 10 },
    { source: 2, target: 6, value: 60 },
    { source: 2, target: 7, value: 20 },
  ],
};

function ScriptSankeyChart() {
  return (
    <Sankey
      width={1500}
      height={500}
      margin={{ top: 20, bottom: 20 }}
      data={data1}
      nodeWidth={15}
      nodePadding={70}
      linkCurvature={0.5}
      iterations={64}
      link={<SankeyLink />}
      node={<SankeyNode containerWidth={960} />}
    >
      <defs>
        <linearGradient id={"linkGradient"}>
          <stop offset="0%" stopColor="rgba(0, 136, 254, 0.5)" />
          <stop offset="100%" stopColor="rgba(0, 197, 159, 0.3)" />
        </linearGradient>
      </defs>
      <Tooltip />
    </Sankey>
  );
}

export default ScriptSankeyChart;
