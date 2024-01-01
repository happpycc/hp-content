import mongoose from "mongoose";

const { Schema, model } = mongoose;

const ContentSchema = new Schema(
  {
    path: { type: String, required: true },
  },
  {
    texts: { type: String, required: true },
  },
  {
    timestamps: {
      createdAt: "create_time",
      updatedAt: "update_time",
    },
  }
);

const ContentModel = model("Content", ContentSchema);

export default ContentModel;
