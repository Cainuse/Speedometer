import React, { useState, useEffect } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import Typography from "@material-ui/core/Typography";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import SyntaxHighlighter from "react-syntax-highlighter";
import { darcula } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { hybrid } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { solarizedLight } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { srcery } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { zenburn } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { solarizedDark } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { sunburst } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { routeros } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { obsidian } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { kimbieDark } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { lioshi } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { far } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { github } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { gruvboxLight } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { Grid } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  heading: {
    fontSize: theme.typography.pxToRem(15),
    fontWeight: theme.typography.fontWeightRegular,
  },
}));

const LineByLineComplexity = ({ codeInformations }) => {
  const classes = useStyles();

  let expandedAcords = [];
  for (let i = 0; i < codeInformations.length; i++) {
    expandedAcords.push(true);
  }

  const [expanded, setExpanded] = useState(expandedAcords);

  const handleChange = (idx) => (_event, _isExpanded) => {
    let expansions = [...expanded];
    expansions[idx] = !expansions[idx];
    setExpanded(expansions);
  };

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        {codeInformations.map((info, index) => {
          return (
            <Grid item xs={6}>
              <Accordion
                expanded={expanded[index]}
                onChange={handleChange(index)}
              >
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel1a-content"
                  id={`panel-${index}-header`}
                >
                  <Typography
                    className={classes.heading}
                  >{`Script Part ${index}`}</Typography>
                </AccordionSummary>
                <AccordionDetails>
                  <Typography>
                    <Typography
                      variant="h2"
                      color={info.proportion > 0.2 ? "error" : "primary"}
                    >
                      {(info.proportion * 100).toString() + "%"}
                    </Typography>
                    <SyntaxHighlighter language="python" style={gruvboxLight}>
                      {info.code}
                    </SyntaxHighlighter>
                  </Typography>
                </AccordionDetails>
              </Accordion>
            </Grid>
          );
        })}
      </Grid>
    </div>
  );
};

export default LineByLineComplexity;
