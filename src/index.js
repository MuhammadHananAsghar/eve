import { createRoot } from 'react-dom/client';
import 'bootstrap/dist/css/bootstrap.min.css';
import App from './components/App';
import './styles/index.css';

// Fonts
import './fonts/euclid_bold.ttf';
import './fonts/euclid_regular.ttf';
import './fonts/euclid_light.ttf';
import './fonts/euclid_semibold.ttf';


createRoot(document.getElementById("root")).render(<App />);