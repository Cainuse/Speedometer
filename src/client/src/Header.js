import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import AppBar from "@material-ui/core/AppBar";
import Toolbar from "@material-ui/core/Toolbar";
import Typography from "@material-ui/core/Typography";
import SpeedIcon from "@material-ui/icons/Speed";

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  speedyIcon: {
    marginRight: theme.spacing(2),
  },
}));

const Header = () => {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <AppBar position="static">
        <Toolbar variant="dense">
          <SpeedIcon className={classes.speedyIcon} />
          <Typography variant="h5" color="inherit">
            Speedometer
          </Typography>
        </Toolbar>
      </AppBar>
    </div>
  );
};

export default Header;
