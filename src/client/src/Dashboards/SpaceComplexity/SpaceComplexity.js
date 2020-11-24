import React from "react";
import { connect } from "react-redux";
import { makeStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Grid from "@material-ui/core/Grid";
import { Box, Typography } from "@material-ui/core";
import MemoryAreaChart from "../Visualizations/Area/MemoryAreaChart";
import FunctionsPieChart from "../Visualizations/Pie/FunctionsPieChart";
import ComposedBarChart from "../Visualizations/Bar/ComposedBarChart";
import ScriptSankeyChart from "../Visualizations/Sankey/ScriptSankeyChart";
import { getFilteredInputData } from "../../constants";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(3),
    textAlign: "center",
    color: theme.palette.text.secondary,
    height: "25rem",
  },
}));

const nDataX = "n";
const nDataY = "total_memory";
const fnDataY = "total_memory";

const SpaceComplexity = ({ dataset }) => {
  const classes = useStyles();

  const nData = getFilteredInputData(dataset, "e2e_memory");

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
            <Typography>Memory Usage Area Chart</Typography>
            <MemoryAreaChart data={nData} xDataKey={nDataX} yDataKey={nDataY} />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper}>
            <Typography>Memory Usage Per Function Pie Chart</Typography>
            <FunctionsPieChart
              data={dataset["function"]["function_memory"]}
              pieDataKey={fnDataY}
            />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={6}>
          <Paper className={classes.paper}>
            <Typography>Memory Usage Per Function Bar Chart</Typography>
            <ComposedBarChart
              data={dataset["function"]["function_memory"]}
              barDataKey={fnDataY}
            />
          </Paper>
        </Grid>
        <Grid item xs={12} sm={12}>
          <Typography>Space Usage Per Script module</Typography>
          <ScriptSankeyChart />
        </Grid>
      </Grid>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    dataset: state.dataset,
  };
};

export default connect(mapStateToProps)(SpaceComplexity);
