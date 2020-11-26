import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Timeline from "@material-ui/lab/Timeline";
import TimelineItem from "@material-ui/lab/TimelineItem";
import TimelineSeparator from "@material-ui/lab/TimelineSeparator";
import TimelineConnector from "@material-ui/lab/TimelineConnector";
import TimelineContent from "@material-ui/lab/TimelineContent";
import TimelineOppositeContent from "@material-ui/lab/TimelineOppositeContent";
import TimelineDot from "@material-ui/lab/TimelineDot";
import DirectionsRunIcon from "@material-ui/icons/DirectionsRun";
import EqualizerIcon from "@material-ui/icons/Equalizer";
import TimelineIcon from "@material-ui/icons/Timeline";
import BubbleChartIcon from "@material-ui/icons/BubbleChart";
import BarChartIcon from "@material-ui/icons/BarChart";
import TrendingUpIcon from "@material-ui/icons/TrendingUp";
import AssessmentIcon from "@material-ui/icons/Assessment";
import TrendingFlatIcon from "@material-ui/icons/TrendingFlat";
import ShowChartIcon from "@material-ui/icons/ShowChart";
import TrendingDownIcon from "@material-ui/icons/TrendingDown";
import GraphicEqIcon from "@material-ui/icons/GraphicEq";
import Paper from "@material-ui/core/Paper";
import Typography from "@material-ui/core/Typography";

const useStyles = makeStyles((theme) => ({
  paper: {
    padding: "6px 16px",
  },
  secondaryTail: {
    backgroundColor: theme.palette.secondary.main,
  },
}));

const iconsList = [
  <DirectionsRunIcon />,
  <EqualizerIcon />,
  <BubbleChartIcon />,
  <TimelineIcon />,
  <BarChartIcon />,
  <TrendingUpIcon />,
  <AssessmentIcon />,
  <TrendingFlatIcon />,
  <ShowChartIcon />,
  <TrendingDownIcon />,
  <TrendingDownIcon />,
  <GraphicEqIcon />,
];

const colorsList = ["grey", "primary", "secondary"];
const variants = ["default", "outlined"];

/**
 * Returns a random number between min (inclusive) and max (exclusive)
 */
const getRandIdx = (min, max) => {
  return Math.floor(Math.random() * (max - min) + min);
};

const ComplexTimelineSeparator = (icon, connector) => {
  const color = colorsList[getRandIdx(0, colorsList.length)];
  const variant = variants[getRandIdx(0, variants.length)];
  return (
    <TimelineSeparator>
      <TimelineDot color={color} variant={variant}>
        {icon}
      </TimelineDot>
      {connector}
    </TimelineSeparator>
  );
};

const ComplexTimelineItem = (time, fn, connector) => {
  const classes = useStyles();
  const icon = iconsList[getRandIdx(0, iconsList.length)];

  return (
    <TimelineItem key={fn}>
      <TimelineOppositeContent>
        <Typography variant="body2" color="textSecondary">
          {time}
        </Typography>
      </TimelineOppositeContent>
      {ComplexTimelineSeparator(icon, connector ? connector : null)}
      <TimelineContent>
        <Paper elevation={3} className={classes.paper}>
          <Typography variant="h6">{fn}</Typography>
        </Paper>
      </TimelineContent>
    </TimelineItem>
  );
};

const ComplexityTimeline = ({ data }) => {
  return (
    <Timeline align="alternate">
      {data.map((d, idx) => {
        return idx !== data.length - 1
          ? ComplexTimelineItem(d.time, d.fn, <TimelineConnector />)
          : ComplexTimelineItem(d.time, d.fn);
      })}
    </Timeline>
  );
};

export default ComplexityTimeline;
