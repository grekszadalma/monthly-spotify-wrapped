import "./../styles/home.css";

export default function Home() {
  return (
    <div className="app">

      {/* Full page background layer */}
      <div className="bg" />

      <div className="home">

        {/* Top bar */}
        <header className="topbar">
          <div className="logo">Monthly Wrapped</div>

          <button className="connect-btn">
            Connect Spotify
          </button>
        </header>

        {/* Hero section */}
        <main className="hero">
          <h1>Your month in music, wrapped.</h1>

          <p>
            See your top songs, artists, and listening minutes in a beautiful story.
          </p>

         <button className="primary-btn" onClick={() => window.location.href = "/wrapped"}>
            View your Wrapped →
         </button>

          <button className="secondary-btn">
            Change month
          </button>
        </main>

        

        {/* Footer */}
        <footer className="month">
          Viewing: June 2026
        </footer>

      </div>
    </div>
  );
}