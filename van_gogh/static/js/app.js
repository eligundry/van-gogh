(function($) {
  var $voteContainer = $('#vote-container');

  function renderVoteContainer() {
    const compiled = Handlebars.templates.vote(PRELOAD);
    $voteContainer.html(compiled);
  }

  function renderVoteResults(results) {
    const compiled = Handlebars.templates.results(results);
    $voteContainer.html(compiled);
  }

  function submitVote(event) {
    event.preventDefault();

    var data = {};

    $.each($voteContainer.find('form').serializeArray(), function(idx, obj) {
      data[obj.name] = obj.value;
    });

    var url = '/api/artists';
    var method = 'POST';

    if (data.artist !== 'other') {
      url = `/api/artists/${data.artist}`;
      method = 'PATCH';
    } else if (!data.name) {
      alert("If you want to vote for another artist, you must enter their name!");
      return;
    }

    $.ajax({
      url: url,
      method: method,
      data: JSON.stringify(data),
      dataType: 'json',
      contentType: 'application/json',
      success: function(data, status, xhr) {
        renderVoteResults(data);
      }
    });
  }

  $voteContainer
    .on('click', '.vote button', submitVote)
    .on('focus', 'input[type="radio"] + input[type="text"]', function(event) {
      event.target.previousElementSibling.checked = true;
      event.target.required = true;
    });

  renderVoteContainer();

})(jQuery);
