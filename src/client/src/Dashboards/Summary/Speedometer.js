import React from "react";
import ReactSpeedometer from "react-d3-speedometer";
import { LABELS } from "../../constants";

const Speedometer = ({ value, valueText }) => {
  return (
    <ReactSpeedometer
      fluidWidth={true}
      height="100%"
      minValue={0}
      maxValue={8}
      segments={8}
      needleHeightRatio={0.72}
      value={value}
      currentValueText={valueText}
      customSegmentLabels={LABELS}
      ringWidth={90}
      needleTransitionDuration={3333}
      needleTransition="easeElastic"
      needleColor={"#3f51b5"}
      textColor={"#555"}
    />
  );
};

export default Speedometer;
