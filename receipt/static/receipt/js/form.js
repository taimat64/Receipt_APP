
  document.addEventListener('DOMContentLoaded', function() {
    // 追加ボタンを取得
    const addButton = document.getElementById('add_item');
    // 追加ボタンのクリックを処理
    addButton.addEventListener('click', function() {
      // ItemフォームのHTMLを取得
      const itemFormHTML = document.getElementById('items').lastElementChild.outerHTML;
      // 新しいItemフォームを追加
      document.getElementById('items').insertAdjacentHTML('beforeend', itemFormHTML);
    });
  });
