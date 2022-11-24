function deleteNote(noteId) {
    fetch("/delete-note", {
      method: "POST",
      body: JSON.stringify({ noteId: noteId }),
    }).then((_res) => {
      window.location.href = "/";
    });
  }


function editNote(noteId) {
  console.log(noteId);

  var noteData = document.getElementById('edit_note'+noteId).value;

  fetch("/edit-note", {
    method: "POST",
    body: JSON.stringify({ noteId: noteId, noteData : noteData}),
  }).then((_res) => {
    window.location.href = "/";
  });
}

