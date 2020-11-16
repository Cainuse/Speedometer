import React, { useState } from "react";
import Paper from "@material-ui/core/Paper";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Typography from "@material-ui/core/Typography";
import Box from "@material-ui/core/Box";
import AssessmentIcon from "@material-ui/icons/Assessment";
import Summary from "./Dashboards/Summary/Summary";
import SpaceComplexity from "./Dashboards/SpaceComplexity/SpaceComplexity";
import TimeComplexity from "./Dashboards/TimeComplexity/TimeComplexity";
import LineByLineComplexity from "./Dashboards/LineByLine/LineByLineComplexity";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
  },
  tabs_appbar: {
    backgroundColor: "#66d9ff",
    color: "white",
  },
}));

const DashTabs = () => {
  const classes = useStyles();
  const [value, setValue] = useState(0);

  const handleChange = (_, newValue) => {
    setValue(newValue);
  };

  return (
    <div className={classes.root}>
      <AppBar position="static" className={classes.tabs_appbar}>
        <Tabs
          variant="fullWidth"
          value={value}
          onChange={handleChange}
          aria-label="nav tabs example"
        >
          <LinkTab
            variant="h5"
            label="Summary"
            href="/summary"
            {...LinkTabProps(0)}
          />
          <LinkTab
            label="Time Complexity"
            href="/timeComplexity"
            {...LinkTabProps(1)}
          />
          <LinkTab
            label="Space Complexity"
            href="/spaceComplexity"
            {...LinkTabProps(2)}
          />
          <LinkTab
            label="Line By Line"
            href="/lineByLineComplexity"
            {...LinkTabProps(3)}
          />
        </Tabs>
      </AppBar>
      <TabPanel value={value} index={0}>
        <Summary />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <TimeComplexity />
      </TabPanel>
      <TabPanel value={value} index={2}>
        <SpaceComplexity />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <LineByLineComplexity codeInformations={[0, 1, 2]} />
      </TabPanel>
    </div>
  );
};

const TabPanel = (props) => {
  const { children, value, index, ...other } = props;

  return (
    <div
      role="tabpanel"
      hidden={value !== index}
      id={`nav-tabpanel-${index}`}
      aria-labelledby={`nav-tab-${index}`}
      {...other}
    >
      {value === index && <Box p={7}>{children}</Box>}
    </div>
  );
};

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

const LinkTabProps = (index) => {
  return {
    id: `nav-tab-${index}`,
    "aria-controls": `nav-tabpanel-${index}`,
  };
};

const LinkTab = (props) => {
  return (
    <Tab
      component="a"
      onClick={(event) => {
        event.preventDefault();
      }}
      {...props}
    />
  );
};

export default DashTabs;
