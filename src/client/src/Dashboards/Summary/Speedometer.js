import React from "react";
import ReactSpeedometer from "react-d3-speedometer";
import { LABELS } from "../../constants";

const Speedometer = ({ value, valueText }) => {
  return (
    <ReactSpeedometer
      fluidWidth={true}
      height="100%"
      minValue={0}
      maxValue={7}
      segments={7}
      needleHeightRatio={0.65}
      value={value}
      currentValueText={valueText}
      customSegmentLabels={LABELS}
      ringWidth={100}
      needleTransitionDuration={3333}
      needleTransition="easeElastic"
      needleColor={"#3f51b5"}
      textColor={"#555"}
    />
  );
};

export default Speedometer;
