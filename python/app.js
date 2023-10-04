const { PythonShell } = require("python-shell");
const express = require("express");

const app = express();

const moviesRouter = express.Router();
app.use("/api/v1/movies", moviesRouter);
const options = {
  scriptPath: "C:/Users/Shahid Bangash/Desktop/python",
};
app.listen(8000, () => {
  console.log("...listening from the port");
});

moviesRouter.route("/").get((req, res) => {
  let page = req.query.page * 1 || 1;
  options.args = [page];

  PythonShell.run("LandingPage.py", options).then((data, err) => {
    if (data[0] === "err")
      res.status(500).json({
        status: "failed",
        message: "Something went Wrong",
      });
    else
      res.status(200).json({
        status: "successful",
        data: data[0],
      });
  });
});

moviesRouter.route("/movie/:id").get((req, res) => {
  options.args = [req.params.id];
  PythonShell.run("Description.py", options).then((data, err) => {
    if (data[0] === "err")
      res.status(500).json({
        status: "failed",
        message: "Something went Wrong",
      });
    else
      res.status(200).json({
        status: "successful",
        data: data[0],
      });
  });
});

moviesRouter.route("/filter/").get((req, res) => {
  let page = req.query.page * 1 || 1;
  let cat = req.query.cat;
  options.args = [page, cat];

  PythonShell.run("Category.py", options).then((data, err) => {
    if (data[0] === "err")
      res.status(500).json({
        status: "failed",
        message: "Something went Wrong",
      });
    else
      res.status(200).json({
        status: "successful",
        data: data[0],
      });
  });
});
moviesRouter.route("/tag/").get((req, res) => {
  let page = req.query.page * 1 || 1;
  let year = req.query.year;
  options.args = [page, year];

  PythonShell.run("ByYear.py", options).then((data, err) => {
    if (data[0] === "err")
      res.status(500).json({
        status: "failed",
        message: "Something went Wrong",
      });
    else
      res.status(200).json({
        status: "successful",
        data: data[0],
      });
  });
});
moviesRouter.route("/query/").get((req, res) => {
  let page = req.query.page * 1 || 1;
  let query = req.query.s;

  options.args = [page, query];

  PythonShell.run("Search.py", options).then((data, err) => {
    if (data[0] === "err")
      res.status(500).json({
        status: "failed",
        message: "Something went Wrong",
      });
    else
      res.status(200).json({
        status: "successful",
        data: data[0],
      });
  });
});
moviesRouter.route("/actors/").get((req, res) => {
  let name = req.query.name;
  let page = req.query.page || 1;
  options.args = [page, name];

  PythonShell.run("ByActor.py", options).then((data, err) => {
    if (data[0] === "err")
      res.status(500).json({
        status: "failed",
        message: "Something went Wrong",
      });
    else
      res.status(200).json({
        status: "successful",
        data: data[0],
      });
  });
});

let movies;
