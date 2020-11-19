import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Timeline from "@material-ui/lab/Timeline";
import TimelineItem from "@material-ui/lab/TimelineItem";
import TimelineSeparator from "@material-ui/lab/TimelineSeparator";
import TimelineConnector from "@material-ui/lab/TimelineConnector";
import TimelineContent from "@material-ui/lab/TimelineContent";
import TimelineOppositeContent from "@material-ui/lab/TimelineOppositeContent";
import TimelineDot from "@material-ui/lab/TimelineDot";
import FastfoodIcon from "@material-ui/icons/Fastfood";
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

const ComplexTimelineSeparator = (icon, connector) => {
  return (
    <TimelineSeparator>
      <TimelineDot>{icon}</TimelineDot>
      {connector}
    </TimelineSeparator>
  );
};

const ComplexTimelineItem = (time, fn, connector) => {
  const classes = useStyles();
  return (
    <TimelineItem>
      <TimelineOppositeContent>
        <Typography variant="body2" color="textSecondary">
          {time}
        </Typography>
      </TimelineOppositeContent>
      {ComplexTimelineSeparator(<FastfoodIcon />, connector)}
      <TimelineContent>
        <Paper elevation={3} className={classes.paper}>
          <Typography variant="h6" component="h1">
            {fn}
          </Typography>
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
