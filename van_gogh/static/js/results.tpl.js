(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['results'] = template({"1":function(container,depth0,helpers,partials,data,blockParams,depths) {
    var helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "  <div class=\"result\">\n    <h4>"
    + alias4(((helper = (helper = helpers.name || (depth0 != null ? depth0.name : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"name","hash":{},"data":data}) : helper)))
    + " ("
    + alias4(((helper = (helper = helpers.vote_count || (depth0 != null ? depth0.vote_count : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"vote_count","hash":{},"data":data}) : helper)))
    + " Vote(s))</h4>\n    <progress value=\""
    + alias4(((helper = (helper = helpers.vote_count || (depth0 != null ? depth0.vote_count : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"vote_count","hash":{},"data":data}) : helper)))
    + "\" max=\""
    + alias4(container.lambda((depths[1] != null ? depths[1].total_votes : depths[1]), depth0))
    + "\"></progress>\n  </div>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data,blockParams,depths) {
    var stack1, helper, alias1=depth0 != null ? depth0 : (container.nullContext || {});

  return "<div class=\"results\">\n  <h2>Results ("
    + container.escapeExpression(((helper = (helper = helpers.total_votes || (depth0 != null ? depth0.total_votes : depth0)) != null ? helper : helpers.helperMissing),(typeof helper === "function" ? helper.call(alias1,{"name":"total_votes","hash":{},"data":data}) : helper)))
    + " (Vote(s)))</h2>\n"
    + ((stack1 = helpers.each.call(alias1,(depth0 != null ? depth0.artists : depth0),{"name":"each","hash":{},"fn":container.program(1, data, 0, blockParams, depths),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "</div>\n";
},"useData":true,"useDepths":true});
})();