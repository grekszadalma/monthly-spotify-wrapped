import { useEffect, useState } from "react";
import "./../styles/wrapped.css";
import { getWrapped } from "./../../api/getWrapped.js";
import TimeSpent from "../components/TimeSpent.jsx";

export default function Wrapped() {
  const [index, setIndex] = useState(0);
  const [data, setData] = useState(null);

  useEffect(() => {
    getWrapped("testuser")
      .then(setData)
      .catch(console.error);
  }, []);

  if (!data) return <div>Loading...</div>;

  const slides = [
    {
      type: "intro",
      data: {
        title: "Your month in music",
        subtitle: "June 2026"
      }
    },
    {
      type: "timespent",
      data: [
        {
          type: "minutes",
          value: Math.round(data.minutes_listened)
        },
        {
          type: "Daily average",
          value: 5
        },
        {
          type: "Streak",
          value: 7
        },
        {
          type: "Biggest Day",
          value: data.biggest_day
        }
        
    ]
    },
   
    {
      type: "sumsongs",
      data: {
        sum: data.top_songs?.length || 0
      }
    },
    {
      type: "topArtist",
      data: {
        title: "Your Top Artist",
        name: data.top_artists?.[0]?.[0] || "Unknown"
      }
    },
    {
      type: "topSong",
      data: {
        title: "Your Top Song",
        name: data.top_songs?.[0]?.name || "Unknown",
        artist: data.top_songs?.[0]?.artist || ""
      }
    },
    {
      type: "topArtistsList",
      data: {
        artists: data.top_artists?.map(([name]) => ({ name })) || []
      }
    },
    {
      type: "topSongsList",
      data: {
        songs: data.top_songs || []
      }
    }
  ];

  const slide = slides[index];

  const nextSlide = () => {
    if (index < slides.length - 1) setIndex(index + 1);
  };

  const prevSlide = () => {
    if (index > 0) setIndex(index - 1);
  };

  const renderSlide = () => {
    switch (slide.type) {
      case "intro":
        return (
          <>
            <h1>{slide.data.title}</h1>
            <p>{slide.data.subtitle}</p>
          </>
        );

      case "timespent":
        return(
        <TimeSpent data={slide.data}/>);


      case "sumsongs":
        return (
          <>
            <p>Total Songs</p>
            <h1>{slide.data.sum}</h1>
          </>
        );

      case "topArtist":
        return (
          <>
            <h1>{slide.data.title}</h1>
            <h2>{slide.data.name}</h2>
            <p>Top artist</p>
          </>
        );

      case "topSong":
        return (
          <>
            <h1>You couldn't stop listening to {slide.data.name} by {slide.data.artist}. You played it 19 times.</h1>
            
          </>
        );

      case "topArtistsList":
        return (
          <>
            <h1>Your top artists</h1>
            <div className="list">
              {slide.data.artists.map((artist, i) => (
                <div key={i} className="song">
                  <strong>{artist.name}</strong>
                </div>
              ))}
            </div>
          </>
        );

      case "topSongsList":
        return (
          <>
            <h1>Your top songs</h1>
            <div className="list">
              {slide.data.songs.map((song, i) => (
                <div key={i} className="song">
                  <strong>{song.name}</strong>
                  <p>{song.artist}</p>
                </div>
              ))}
            </div>
          </>
        );

      default:
        return null;
    }
  };

  return (
    <div className="wrapped" onClick={nextSlide}>
      <div className="slide">{renderSlide()}</div>

      <div className="controls">
        <button onClick={(e) => { e.stopPropagation(); prevSlide(); }}>
          Prev
        </button>

        <div className="dots">
          {slides.map((_, i) => (
            <div key={i} className={`dot ${i === index ? "active" : ""}`} />
          ))}
        </div>

        <button onClick={(e) => { e.stopPropagation(); nextSlide(); }}>
          Next
        </button>
      </div>
    </div>
  );
}