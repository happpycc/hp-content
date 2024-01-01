import express from "express";
import {
  getContents,
} from "./controller.js";

const router = express.Router();

router.route("/").get(getContents);

export default router;
