import ContentModel from "./model.js";

export const getContents = async (_, res) => {
  await ContentModel.find()
    .then((memos) => res.json(memos))
    .catch((err) => {
      console.log(err);
      res.status(500).send("Server error");
    });
};
