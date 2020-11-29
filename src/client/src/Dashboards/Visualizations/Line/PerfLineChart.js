import { Button } from "@material-ui/core";
import React, { PureComponent } from "react";
import { getRandomColor } from "../../../constants";
import {
  Label,
  LineChart,
  Line,
  CartesianGrid,
  XAxis,
  YAxis,
  Tooltip,
  ReferenceArea,
  ResponsiveContainer,
  Legend,
} from "recharts";
import ZoomOutIcon from "@material-ui/icons/ZoomOut";

export default class PerfLineChart extends PureComponent {
  constructor(props) {
    super(props);
    const data = props.data.sort((a, b) => a["n"] - b["n"]);
    this.state = {
      data,
      lineColours: this.getLineColours(data),
      left: "dataMin",
      right: "dataMax",
      refAreaLeft: "",
      refAreaRight: "",
      top: "auto",
      bottom: 0,
      animation: true,
    };
  }

  getYTypes(data) {
    let yTypes = Object.keys(data[0] ? data[0] : {})
      .map((key, i) => {
        return i !== 0 ? key : null;
      })
      .filter((key) => key !== null);
    return yTypes;
  }

  filterYValues(data) {
    const zeroKeys = Object.keys(data[0]).filter((key) => {
      return data.every((dataObj) => dataObj[key] <= 0);
    });

    let filteredData = data;
    zeroKeys.forEach((key) => {
      filteredData.forEach((dataObj) => delete dataObj[key]);
    });
    return filteredData;
  }

  getMaxScriptTime(data) {
    return Math.max.apply(
      Math,
      data.map((o) => {
        return o.total_runtime;
      })
    );
  }

  getLineColours(data) {
    let lineColours = {};
    this.getYTypes(data).forEach((yType) => {
      lineColours[yType] = getRandomColor();
    });

    return lineColours;
  }

  getAxisYDomain(from, to, ref, offset) {
    const { data } = this.state;
    const fromElementIdx = data.findIndex((d) => d["n"] === from);
    const toElementIdx = data.findIndex((d) => d["n"] === to);

    let [bottom, top] = [Number.MAX_VALUE, -1];
    const refData = data.slice(
      fromElementIdx - 1 > 0 ? fromElementIdx - 1 : 0,
      toElementIdx + 1 <= data.length ? toElementIdx + 1 : toElementIdx
    );

    refData.forEach((d) => {
      if (d[ref] > top) top = d[ref];
      if (d[ref] < bottom) bottom = d[ref];
    });

    return [(bottom | 0) - offset, (top | 0) + offset];
  }

  zoom() {
    let { refAreaLeft, refAreaRight, data } = this.state;

    if (refAreaLeft === refAreaRight || refAreaRight === "") {
      this.setState(() => ({
        refAreaLeft: "",
        refAreaRight: "",
      }));
      return;
    }

    // xAxis domain
    if (refAreaLeft > refAreaRight)
      [refAreaLeft, refAreaRight] = [refAreaRight, refAreaLeft];

    // yAxis domain
    let [bottom, top] = [Number.MAX_VALUE, -1];
    for (let yType of this.getYTypes(data)) {
      const [currBottom, currTop] = this.getAxisYDomain(
        refAreaLeft,
        refAreaRight,
        yType,
        1
      );
      [bottom, top] = [Math.min(bottom, currBottom), Math.max(top, currTop)];
    }

    this.setState(() => ({
      refAreaLeft: "",
      refAreaRight: "",
      data: data.slice(),
      left: refAreaLeft,
      right: refAreaRight,
      bottom,
      top,
    }));
  }

  zoomOut() {
    const { data } = this.state;
    this.setState(() => ({
      data: data.slice(),
      refAreaLeft: "",
      refAreaRight: "",
      left: "dataMin",
      right: "dataMax",
      top: "auto",
      bottom: 0,
    }));
  }

  render() {
    const {
      data,
      lineColours,
      left,
      right,
      refAreaLeft,
      refAreaRight,
      top,
      bottom,
    } = this.state;

    return (
      <div
        className="highlight-bar-charts"
        style={{
          userSelect: "none",
          width: "90%",
          height: "80%",
          marginLeft: "6%",
          marginBottom: "5%",
        }}
      >
        <Button
          onClick={this.zoomOut.bind(this)}
          variant="contained"
          color="primary"
          size="small"
          startIcon={<ZoomOutIcon />}
          style={{
            textTransform: "none",
            marginRight: "80%",
          }}
        >
          Zoom Out
        </Button>

        <ResponsiveContainer>
          <LineChart
            data={this.filterYValues(data)}
            onMouseDown={(e) =>
              this.setState({ refAreaLeft: e ? e.activeLabel : "" })
            }
            onMouseMove={(e) =>
              this.state.refAreaLeft &&
              this.setState({ refAreaRight: e ? e.activeLabel : "" })
            }
            onMouseUp={this.zoom.bind(this)}
            margin={{ top: 5, right: 10, left: 50, bottom: 37 }}
          >
            <CartesianGrid strokeDasharray="3 3" />
            <XAxis
              allowDataOverflow
              dataKey="n"
              domain={[left, right]}
              type="number"
            >
              <Label value="Input Size (n)" offset={-1} position="bottom" />
            </XAxis>
            <YAxis
              allowDataOverflow
              domain={[bottom, top]}
              type="number"
              yAxisId="1"
            >
              <Label
                value={this.props.yLabel}
                offset={25}
                position="left"
                angle={-90}
              />
            </YAxis>
            <Tooltip />
            {this.getYTypes(data).map((yTypeKey, idx) => {
              return (
                <Line
                  key={idx}
                  yAxisId="1"
                  type="natural"
                  dataKey={yTypeKey}
                  stroke={lineColours[yTypeKey]}
                  animationDuration={300}
                />
              );
            })}

            <Legend align="right" verticalAlign="top" height={50} />

            {refAreaLeft && refAreaRight ? (
              <ReferenceArea
                yAxisId="1"
                x1={refAreaLeft}
                x2={refAreaRight}
                strokeOpacity={0.3}
              />
            ) : null}
          </LineChart>
        </ResponsiveContainer>
      </div>
    );
  }
}
