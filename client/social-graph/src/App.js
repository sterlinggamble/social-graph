import './App.css';
import Navbar from './components/navbar/Navbar';
import Graph from './components/graph/Graph';

function App() {
  return (
    <div className="App">
      <Navbar />
      <Graph title={'New Graph'} />
    </div>
  );
}

export default App;
