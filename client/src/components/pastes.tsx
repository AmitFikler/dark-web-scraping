import { Paste } from '../../@types/paste';
function Pastes({ paste }: { paste: Paste }) {
  return (
    <div className="paste" id={paste._id}>
      <div className="paste-header">
        <div className="paste-title">
          <h4>{paste.Title}</h4>
        </div>
        <div className="paste-info">
          <div className="paste-info-date">
            <span>{paste.Date}</span>
          </div>
          <div>
            <span>{paste.Author}</span>
          </div>
        </div>
      </div>
      <div className="paste-content">
        <div className="paste-content-text">
          <pre>{paste.Content}</pre>
        </div>
      </div>
    </div>
  );
}

export default Pastes;
