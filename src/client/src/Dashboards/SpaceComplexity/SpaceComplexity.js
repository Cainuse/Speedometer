import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: "center",
    color: theme.palette.text.secondary,
  },
}));

const SpaceComplexity = () => {
  const classes = useStyles();

  const defaultProps = {
    bgcolor: "background.paper",
    m: 1,
    style: { width: "100%", height: "2rem", marginBottom: "3%" },
    borderColor: "grey.500",
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Space Complexity Analysis for 'test.py'
      </Box>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            Memory usage of script over time line of program execution
            {/* TODO: Make a card with proper titles,
            descrition, maybe buttons for interactions,
            properly formatted */}
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper}>
            Function specific memory pie chart
            {/* TODO: Make a card with proper titles,
            descrition, maybe buttons for interactions,
            properly formatted */}
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper}>
            Script big-O memory complexity line chart
            {/* TODO: Make a card with proper titles,
            descrition, maybe buttons for interactions,
            properly formatted */}
          </Paper>
        </Grid>
        <Grid item xs={12} sm={12}>
          <Paper className={classes.paper}>
            Memory usage per module SankeyChart
            {/* TODO: Make a card with proper titles,
            descrition, maybe buttons for interactions,
            properly formatted */}
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
};

export default SpaceComplexity;
