(function() {
  var template = Handlebars.template, templates = Handlebars.templates = Handlebars.templates || {};
templates['vote'] = template({"1":function(container,depth0,helpers,partials,data) {
    var helper, alias1=depth0 != null ? depth0 : (container.nullContext || {}), alias2=helpers.helperMissing, alias3="function", alias4=container.escapeExpression;

  return "  <div class=\"form-check\">\n    <label for=\"artist-"
    + alias4(((helper = (helper = helpers.id || (depth0 != null ? depth0.id : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"id","hash":{},"data":data}) : helper)))
    + "\">\n      <input type=\"radio\" name=\"artist\" id=\"artist-"
    + alias4(((helper = (helper = helpers.id || (depth0 != null ? depth0.id : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"id","hash":{},"data":data}) : helper)))
    + "\" value=\""
    + alias4(((helper = (helper = helpers.id || (depth0 != null ? depth0.id : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"id","hash":{},"data":data}) : helper)))
    + "\">\n      "
    + alias4(((helper = (helper = helpers.name || (depth0 != null ? depth0.name : depth0)) != null ? helper : alias2),(typeof helper === alias3 ? helper.call(alias1,{"name":"name","hash":{},"data":data}) : helper)))
    + "\n    </label>\n  </div>\n";
},"compiler":[7,">= 4.0.0"],"main":function(container,depth0,helpers,partials,data) {
    var stack1;

  return "<form class=\"vote\">\n  <h2>Vote</h2>\n"
    + ((stack1 = helpers.each.call(depth0 != null ? depth0 : (container.nullContext || {}),(depth0 != null ? depth0.artists : depth0),{"name":"each","hash":{},"fn":container.program(1, data, 0),"inverse":container.noop,"data":data})) != null ? stack1 : "")
    + "  <div class=\"form-check\">\n    <label for=\"artist-other\">\n      <input id=\"artist-other\" type=\"radio\" name=\"artist\" value=\"other\">\n      <input type=\"text\" placeholder=\"Other\" name=\"name\">\n    </label>\n  </div>\n  <button class=\"btn btn-primary\" type=\"submit\">\n    Submit Vote\n  </button>\n</form>\n";
},"useData":true});
})();