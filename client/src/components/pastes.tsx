import { Paste } from '../../@types/paste';

function Pastes({ paste }: { paste: Paste }) {
  return (
    <div className="paste" id={paste._id}>
      <div className="paste-header">
        <h4>{paste.Title}</h4>
        <span>{paste.Date} | </span>
        <span>{paste.Author}</span>
      </div>
      <div className="paste-content">
        <div>{paste.Content}</div>
      </div>
    </div>
  );
}

export default Pastes;
