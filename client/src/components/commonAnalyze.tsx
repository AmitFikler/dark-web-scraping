import { Common } from '../../@types/common';
function CommonWords({ common }: { common: Common | undefined }) {
  return (
    <>
      {common ? (
        <>
          <div>bitcoin: {common['total_pastes_bitcoin']}</div>
          <div>porn: {common['total_pastes_porn']}</div>
          <div>gun: {common['total_pastes_gun']}</div>
          <div>credit cards: {common['total_pastes_creditcard']}</div>
          <div>drug: {common['total_pastes_drug']}</div>
          <div>hack: {common['total_pastes_hack']}</div>
          <div>leak: {common['total_pastes_leak']}</div>
          <div>child: {common['total_pastes_child']}</div>
          <div>dark: {common['total_pastes_dark']}</div>
        </>
      ) : (
        <h1>common</h1>
      )}
    </>
  );
}

export default CommonWords;
