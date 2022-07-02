import React, { useEffect, useState } from "react";
import { Spinner } from 'react-bootstrap';
import { useLocation } from 'react-router-dom';
import Card from './Card';
import "../styles/Main.css";

export const Main = () => {
  const API = "https://youtubeapibyhanan.herokuapp.com/api";
  const [videos, setVideos] = useState([]);
  const [loading, setLoading] = useState(true);
  const { state } = useLocation();
  const { query } = state ? state : "chota bheem";

  const fetchData = async () => {
    setLoading(true)
    const response = await fetch(`${API}?query=${query}`);
    const data = await response.json();
    setVideos(data['videos']);
    setLoading(false)
  }

  useEffect(() => {
    fetchData()
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [query])



  return (
    <div className="main">
      {loading ? <Spinner animation="grow" variant="warning" className="spinner" /> : <div className="video-gallery">
        {videos.length > 0 ? videos.map((video)=> 
        <Card owner={video.owner_name} thumb={video.video_thumb} cimage={video.channel_img} title={video.video_title} views={video.video_views} date={video.pub_date} id={video.video_id} mtitle={video.main_title} />
        ) : ''}
      </div>}
    </div>
  );
};
