import React, { PureComponent } from "react";
import {
  AreaChart,
  Area,
  Label,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

export default class MemoryAreaChart extends PureComponent {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <ResponsiveContainer width="100%" height="95%">
        <AreaChart
          data={this.props.data}
          margin={{
            top: 20,
            right: 20,
            bottom: 30,
            left: 20,
          }}
        >
          <CartesianGrid strokeDasharray="3 3" />
          <XAxis dataKey={this.props.xDataKey}>
            <Label value="Input Size (n)" offset={2} position="bottom" />
          </XAxis>
          <YAxis>
            <Label
              value="Memory Usage (MB)"
              offset={0}
              position="left"
              angle={-90}
            />
          </YAxis>
          <Tooltip />
          <Area
            type="monotone"
            dataKey={this.props.yDataKey}
            stroke="#8884d8"
            fill="#8884d8"
          />
        </AreaChart>
      </ResponsiveContainer>
    );
  }
}
