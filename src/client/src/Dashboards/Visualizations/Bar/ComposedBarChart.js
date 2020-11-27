import React, { PureComponent } from "react";
import {
  ComposedChart,
  Line,
  Area,
  Label,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  Legend,
  ResponsiveContainer,
} from "recharts";

export default class ComposedBarChart extends PureComponent {
  constructor(props) {
    super(props);
  }

  render() {
    return (
      <ResponsiveContainer width="100%" height="95%">
        <ComposedChart
          data={this.props.data}
          margin={{
            top: 20,
            right: 20,
            bottom: 30,
            left: 20,
          }}
        >
          <CartesianGrid stroke="#f5f5f5" />
          <XAxis dataKey="name">
            <Label value="Function" offset={0} position="bottom" />
          </XAxis>
          <YAxis>
            <Label
              value={this.props.yLabel}
              offset={12}
              position="left"
              angle={-90}
            />
          </YAxis>
          <Tooltip />
          <Legend align="right" verticalAlign="top" height={30} />
          <Bar dataKey={this.props.barDataKey} barSize={20} fill="#413ea0" />
          <Line
            type="monotone"
            dataKey={this.props.barDataKey}
            stroke="#ff7300"
          />
        </ComposedChart>
      </ResponsiveContainer>
    );
  }
}
