import React, { useState } from "react";
import { makeStyles } from "@material-ui/core/styles";
import { connect } from "react-redux";
import Accordion from "@material-ui/core/Accordion";
import AccordionSummary from "@material-ui/core/AccordionSummary";
import AccordionDetails from "@material-ui/core/AccordionDetails";
import ExpandMoreIcon from "@material-ui/icons/ExpandMore";
import { Box, Typography } from "@material-ui/core";
import SyntaxHighlighter from "react-syntax-highlighter";
import { gruvboxLight } from "react-syntax-highlighter/dist/esm/styles/hljs";
import { Grid } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  root: {
    width: "100%",
  },
  heading: {
    fontSize: theme.typography.pxToRem(16),
    fontWeight: theme.typography.fontWeightRegular,
  },
}));

const LineByLineComplexity = ({ dataset }) => {
  const classes = useStyles();
  const timeThreshold = 5;

  const [expanded, setExpanded] = useState(
    dataset["line_by_line"]["line_by_line_runtime"].map(() => {
      return true;
    })
  );

  const defaultProps = {
    bgcolor: "background.paper",
    m: 1,
    style: { width: "100%", height: "2rem", marginBottom: "1%" },
    borderColor: "grey.500",
  };

  const handleChange = (idx) => (_event, _isExpanded) => {
    let expansions = [...expanded];
    expansions[idx] = !expansions[idx];
    setExpanded(expansions);
  };

  const getSnippetFileName = (lines) => {
    return lines && lines.length > 0 ? lines[0]["fileName"] : "";
  };

  const getLinesOfLargeTime = (lines) => {
    const max = lines.filter((lineObj) => {
      return lineObj["total_runtime"] > timeThreshold;
    });
    return max.length > 0 ? max.map((lineObj) => lineObj["line"]) : [];
  };

  const getCodeSnippet = (lines, line) => {
    const lineObj = lines.find((lineObj) => lineObj.line == line);
    return lineObj.code;
  };

  const getPythonSyntaxCode = (lines, codeSnippet, lineNum) => {
    const maxTimeLines = getLinesOfLargeTime(lines);
    return (
      <SyntaxHighlighter
        language="python"
        children={codeSnippet}
        showLineNumbers={true}
        startingLineNumber={lineNum}
        wrapLongLines={true}
        style={gruvboxLight}
        customStyle={{
          marginTop: 0,
          marginBottom: 0,
          marginRight: 20,
          minWidth: "1em",
        }}
        lineProps={(lineNumber) => {
          let style = { display: "block", minWidth: "1em" };
          if (maxTimeLines.includes(lineNumber)) {
            style.backgroundColor = "#F74A25";
          }
          return { style };
        }}
      />
    );
  };

  const getPythonCodeProportionElement = (lines, line) => {
    const lineObj = lines.find((lineObj) => lineObj.line == line);
    const maxTimeLines = getLinesOfLargeTime(lines);
    return maxTimeLines.includes(line) ? (
      <Typography
        variant="h3"
        color={lineObj["total_runtime"] > timeThreshold ? "error" : "primary"}
        style={{ fontSize: 25, paddingLeft: "40%", paddingTop: "2%" }}
      >
        {`${lineObj["total_runtime"]}%`}
      </Typography>
    ) : (
      <Typography variant="h3" style={{ height: "2rem" }} />
    );
  };

  const getLastLineNumber = (lines) => {
    return lines[lines.length - 1].line;
  };

  const getAccordDetails = (lines) => {
    let codeProportionElements = [];
    let codeSyntaxElements = [];
    const lastLine = getLastLineNumber(lines);

    let currLine = 1;
    while (currLine <= lastLine) {
      const codeSnippet = getCodeSnippet(lines, currLine);
      const pyCode = getPythonSyntaxCode(lines, codeSnippet, currLine);
      codeSyntaxElements.push(pyCode);

      const codeProportionEl = getPythonCodeProportionElement(lines, currLine);
      codeProportionElements.push(codeProportionEl);

      currLine++;
    }

    return (
      <Grid container>
        <Grid item xs={1}>
          {codeProportionElements}
        </Grid>
        <Grid item xs={11}>
          {codeSyntaxElements}
        </Grid>
      </Grid>
    );
  };

  return (
    <div className={classes.root}>
      <Box borderBottom={1} {...defaultProps}>
        Line by Line Analysis for {dataset["script_name"]}
      </Box>
      <Grid container spacing={3}>
        {dataset["line_by_line"]["line_by_line_runtime"].map((lines, index) => {
          const fileName = getSnippetFileName(lines);

          return (
            <Grid item xs={12}>
              <Accordion
                expanded={expanded[index]}
                onChange={handleChange(index)}
                elevation={5}
              >
                <AccordionSummary
                  expandIcon={<ExpandMoreIcon />}
                  aria-controls="panel1a-content"
                  id={`panel-${index}-header`}
                >
                  <Typography
                    className={classes.heading}
                  >{`Script File ${fileName}`}</Typography>
                </AccordionSummary>
                <AccordionDetails>{getAccordDetails(lines)}</AccordionDetails>
              </Accordion>
            </Grid>
          );
        })}
      </Grid>
    </div>
  );
};

const mapStateToProps = (state) => {
  return {
    dataset: state.dataset,
  };
};

export default connect(mapStateToProps)(LineByLineComplexity);
