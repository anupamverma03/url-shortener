import { useState } from "react"
import axios from "axios"
import "./App.css"

function App() {

  const [url, setUrl] = useState("")
  const [shortUrl, setShortUrl] = useState("")

  const shortenUrl = async () => {

    try {

      const res = await axios.post("http://127.0.0.1:8000/shorten", {
        original_url: url
      })

      setShortUrl(res.data.short_url)

    } catch (error) {
      alert("Error shortening URL")
    }
  }

  return (
    <div className="container">

      <h1>URL Shortener</h1>

      <input
        type="text"
        placeholder="Enter long URL"
        value={url}
        onChange={(e) => setUrl(e.target.value)}
      />

      <button onClick={shortenUrl}>Shorten URL</button>

      {shortUrl && (
        <div className="result">
          <p>Short URL:</p>
          <a href={shortUrl} target="_blank">{shortUrl}</a>
        </div>
      )}

    </div>
  )
}

export default App