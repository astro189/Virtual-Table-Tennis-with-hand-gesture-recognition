# Virtual-Table-Tennis-with-hand-gesture-recognition
<H2>Steps to complete the project</H2>
<li>Hand Detection using Mediapipe</li>
<li>extracting the coordinates of the wrist joint</li>
<li>Passing the coordinates to the unity game files using UDP</li>
<li>Passing the position of the player object as the coordinates of the wrist</li>

<H3>Hand detection using Mediapipe</H3>
<p>MediaPipe is a cross-platform pipeline framework to build custom machine learning solutions for live and streaming media. The framework was open-sourced by Google and is currently in the alpha stage.</p>
<p>The main reason to use mediapipe is that it is easy to learn and though in the alpha stage is extremly reliable.</p>

<H3>Extracting the coordinates</H3>
<p>The coordinates of the wrist can be extracted using the landmarks of the hand provided by the Mediapipe library</p>

<H3>Passing coordinates to unity</H3>
<p>Here we use the UDP communication protocol to transfer the coordinates to the unity files</p>
<p>The User Datagram Protocol, or UDP, is a communication protocol used across the Internet for especially time-sensitive transmissions such as video playback or DNS lookups. It speeds up communications by not formally establishing a connection before data is transferred. This allows data to be transferred very quickly.</p>

<p>Though by using UDP there is a risk of drop of packets of data during transmission,it still proves to be a better choice in this case due to the how quickly it transmits the data </p>

<H3>Using the coordinates to move the player</H3>

<p>Our last step is to use the received coordinates to move the player object.This can be done by passing the position of the object as the received coordinates.</p>

<video width="320" height="240" autoplay>
  <source src="movie.mp4" type="video/mp4">
  <source src="movie.ogg" type="video/ogg">
Your browser does not support the video tag.
</video>
