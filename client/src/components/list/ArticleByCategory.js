import React, { useEffect, useState } from "react";
import ArticleCard from "../article-card";
import axios from "axios";
import "./style.css";

const ArticleByCategory = (props) => {
  const [data, setData] = useState([]);
  const fetchPost = async () => {
    var key = Object.keys(props.match.params)
    var value = Object.values(props.match.params)
    const response = await axios.get(`http://127.0.0.1:8000/article/?${key}=${value}`);
    setData(response.data);
  };
  useEffect(() => {
    fetchPost();
  }, []);

  const renderResult = () => {
    return data.map((article) => {
      return <ArticleCard key={article.id} article={article} />;
    });
  };
  return <div className="content">{renderResult()}</div>;
};
export default ArticleByCategory;
