
function execute_it(inputfilename){
  var loaded = 0
  //maximum
  var maxi = 0;
  d3.csv("20130526_dump_1000_random.csv", type, function(error, data) {
    maxi = d3.max(data, function(d) { return d.amount; });
    if (++loaded == 2) {
      draw(inputfilename, maxi)
    }

  });
  d3.csv('20130526_dump_new_algorithm_1000.csv', type, function(error, data) {
    maxi = Math.max(d3.max(data, function(d) { return d.amount; }),maxi);
    maxi = Math.ceil(maxi/100) * 100
    if (++loaded == 2) {
      draw(inputfilename, maxi)
    }
  });

}
function draw(inputfilename, maxi) {
  var svg1 = d3.select("svg") .remove();
  var margin = {top: 40, right: 20, bottom: 30, left: 40},
      width = 1300 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

  var formatPercent = d3.format(".0%");

  var x = d3.scale.ordinal()
      .rangeRoundBands([0, width], .1);

  var y = d3.scale.linear()
      .range([height, 0]);

  var xAxis = d3.svg.axis()
      .scale(x)
      .orient("bottom");

  var yAxis = d3.svg.axis()
      .scale(y)
      .orient("left")
      .tickFormat(d3.format("d"));

  var tip = d3.tip()
    .attr('class', 'd3-tip')
    .offset([-10, 0])
    .html(function(d) {
      return "<strong>amount:</strong> <span style='color:#fff'>" + d.amount + "</span>";
    })

  var svg = d3.select("body").append("svg")
      .attr("width", width + margin.left + margin.right)
      .attr("height", height + margin.top + margin.bottom)
    .append("g")
      .attr("transform", "translate(" + margin.left + "," + margin.top + ")");

  svg.call(tip);
  if (inputfilename==""){
    inputfilename = "1000_output.csv";
  }
  
  d3.csv(inputfilename, type, function(error, data) {

    x.domain(data.map(function(d) { return d.rank; }));
    y.domain([0, maxi]);
  //d3.max(data, function(d) { return d.amount; })])
    svg.append("g")
        .attr("class", "x axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis)
        .append("text")
        .attr("x", 600)
        .attr("y", 30)
        .style("text-anchor-", "middle")
        .text("rank");

    svg.append("g")
        .attr("class", "y axis")
        .call(yAxis)
      .append("text")
        .attr("transform", "rotate(-90)")
        .attr("y", 6)
        .attr("dy", ".71em")
        .style("text-anchor-", "end")
        .text("amount");

    svg.selectAll(".bar")
        .data(data)
      .enter().append("rect")
        .attr("class", "bar")
        .attr("x", function(d) { return x(d.rank); })
        .attr("width", x.rangeBand())
        .attr("y", function(d) { return y(d.amount); })
        .attr("height", function(d) { return height - y(d.amount); })
        .on('mouseover', tip.show)
        .on('mouseout', tip.hide)

  });
}

function type(d) {
    d.amount = +d.amount;
    return d;
}

execute_it("");