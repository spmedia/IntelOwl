(this.webpackJsonpintelowl=this.webpackJsonpintelowl||[]).push([[10],{558:function(e,t,a){"use strict";a.d(t,"d",(function(){return r})),a.d(t,"j",(function(){return i})),a.d(t,"e",(function(){return s})),a.d(t,"k",(function(){return c})),a.d(t,"c",(function(){return l})),a.d(t,"h",(function(){return o})),a.d(t,"b",(function(){return d})),a.d(t,"g",(function(){return u})),a.d(t,"i",(function(){return b})),a.d(t,"f",(function(){return j})),a.d(t,"a",(function(){return m}));var n=a(15),r={file:"#ed896f",observable:"#42796f"},i={WHITE:"#FFFFFF",GREEN:"#33FF00",AMBER:"#FFC000",RED:"#FF0033"},s={ip:"#9aa66c",url:"#7da7d3",domain:"#8070ed",hash:"#ed896f",generic:"#733010"},c={WHITE:"TLP: use all analyzers",GREEN:"TLP: disable analyzers that could impact privacy",AMBER:"TLP: disable analyzers that could impact privacy and limit access to my organization",RED:"TLP: disable analyzers that could impact privacy, limit access to my organization and do not use any external service"},l={pending:"light",running:"secondary",killed:"gray",reported_with_fails:"warning",reported_without_fails:"success",failed:"danger"},o=Object(n.a)(Object(n.a)({},l),{pending:"light",running:"secondary",killed:"gray",success:"success",failed:"danger"}),d=["pending","running","reported_with_fails","reported_without_fails","killed","failed"],u=["PENDING","RUNNING","KILLED","SUCCESS","FAILED"],b=Object.keys(i),j=Object.keys(s),m=j.concat("file")},560:function(e,t,a){"use strict";a.d(t,"a",(function(){return l}));var n=a(15),r=a(60),i=(a(1),a(527)),s=a(7),c=["tag"];function l(e){var t=e.tag,a=Object(r.a)(e,c);return Object(s.jsx)(i.a,Object(n.a)(Object(n.a)({style:{backgroundColor:t.color}},a),{},{children:t.label}))}},561:function(e,t,a){"use strict";a.d(t,"a",(function(){return o}));var n=a(15),r=a(60),i=(a(1),a(610)),s=a(7),c=["node"],l=["node"];function o(e){return Object(s.jsx)(i.a,{children:e,components:{em:function(e){e.node;var t=Object(r.a)(e,c);return Object(s.jsx)("i",Object(n.a)({className:"text-code"},t))},a:function(e){e.node;var t=Object(r.a)(e,l);return Object(s.jsx)("a",Object(n.a)({target:"_blank",className:"link-primary"},t))}}})}},562:function(e,t,a){"use strict";a.d(t,"a",(function(){return n.a})),a.d(t,"e",(function(){return r.a})),a.d(t,"b",(function(){return h})),a.d(t,"c",(function(){return O})),a.d(t,"d",(function(){return y}));var n=a(560),r=a(561),i=a(15),s=a(60),c=(a(1),a(5)),l=a.n(c),o=a(33),d=a(64),u=a(102),b=a(520),j=a(558),m=a(7),f=["status","className"],v={pending:o.s,running:u.e,reported_with_fails:o.A,success:o.d,reported_without_fails:o.d,killed:o.r,failed:d.f};function h(e){var t=e.status,a=e.className,n=Object(s.a)(e,f),r=t.toLowerCase(),c=(null===j.h||void 0===j.h?void 0:j.h[r])||"light",d=(null===v||void 0===v?void 0:v[r])||o.e,u=l()("text-".concat(c),a);return Object(m.jsxs)(m.Fragment,{children:[Object(m.jsx)(d,Object(i.a)({id:"statusicon-".concat(r),className:u},n)),Object(m.jsx)(b.a,{target:"statusicon-".concat(r),trigger:"hover",className:"p-0 m-0",children:r})]})}h.defaultProps={className:null};var g=["status","className"];function O(e){var t=e.status,a=e.className,n=Object(s.a)(e,g),r=t.toLowerCase(),c=(null===j.h||void 0===j.h?void 0:j.h[r])||"light",o=l()("status-tag","bg-".concat(c),a);return Object(m.jsx)("span",Object(i.a)(Object(i.a)({className:o,title:t},n),{},{children:t.toUpperCase()}))}O.defaultProps={className:null};var p=a(527),x=["value"];function y(e){var t=e.value,a=Object(s.a)(e,x),n="tlptag-badge__".concat(t),r=(null===j.j||void 0===j.j?void 0:j.j[t])||"#dfe1e2",c=(null===j.k||void 0===j.k?void 0:j.k[t])||"invalid";return t?Object(m.jsxs)(p.a,Object(i.a)(Object(i.a)({id:n,style:{backgroundColor:r,color:"black",borderRadius:0,userSelect:"none"}},a),{},{children:[t,Object(m.jsx)(b.a,{target:n,placement:"top",fade:!1,children:c})]})):null}},614:function(e,t,a){"use strict";a.r(t),a.d(t,"default",(function(){return v}));var n=a(21),r=(a(1),a(549)),i=a(529),s=a(559),c=a.n(s),l=a(22),o=a(34),d=a(116),u=a.n(d),b=a(562),j=a(558),m=a(7),f={columns:[{Header:function(){return null},id:"viewJobBtnHeader",accessor:"id",maxWidth:50,disableSortBy:!0,Cell:function(e){var t=e.value;return Object(m.jsx)(l.q,{id:t,href:"/jobs/".concat(t),tooltip:"View Job Report"})}},{Header:"Created",id:"received_request_time",accessor:"received_request_time",Cell:function(e){var t=e.value;return Object(m.jsx)(u.a,{fromNow:!0,withTitle:!0,date:t,titleFormat:"Do MMMM YYYY"})},maxWidth:125},{Header:"Finished",id:"finished_analysis_time",accessor:"finished_analysis_time",Cell:function(e){var t=e.value;return Object(m.jsx)(u.a,{fromNow:!0,withTitle:!0,date:t,titleFormat:"Do MMMM YYYY"})},maxWidth:125},{Header:"User",id:"user",accessor:"user.username",Cell:function(e){var t=e.value,a=e.row.original;return Object(m.jsx)(l.D,{id:"table-user-".concat(null===a||void 0===a?void 0:a.id),value:t},"table-user-".concat(null===a||void 0===a?void 0:a.id))},disableSortBy:!0,Filter:l.j,minWidth:125},{Header:"Name",id:"name",accessor:function(e){return e.observable_name||e.file_name},Cell:function(e){var t=e.value,a=e.row.original;return Object(m.jsx)(l.D,{id:"table-name-".concat(null===a||void 0===a?void 0:a.id),value:t},"table-name-".concat(null===a||void 0===a?void 0:a.id))},disableSortBy:!0,Filter:l.j,minWidth:175},{Header:"MD5",id:"md5",accessor:"md5",Cell:function(e){var t=e.value,a=e.row.original;return Object(m.jsx)(l.D,{id:"table-md5-".concat(null===a||void 0===a?void 0:a.id),value:t},"table-md5-".concat(null===a||void 0===a?void 0:a.id))},disableSortBy:!0,Filter:l.j,minWidth:175},{Header:"Settings",columns:[{Header:"Type",id:"type",accessor:function(e){return e.observable_classification||e.file_mimetype},disableSortBy:!0,Filter:l.C,selectOptions:j.a,minWidth:125},{Header:"TLP",id:"tlp",accessor:"tlp",Cell:function(e){var t=e.value;return Object(m.jsx)(b.d,{value:t})},disableSortBy:!0,Filter:l.C,selectOptions:j.i,minWidth:125},{Header:"Tags",id:"tags",accessor:"tags",Cell:function(e){return e.value.map((function(e){return Object(m.jsx)(b.a,{tag:e,className:"ml-2"},"jobtable-tags-".concat(e.label))}))},disableSortBy:!0,Filter:l.j,filterValueAccessorFn:function(e){return e.map((function(e){return e.label}))},minWidth:150}]},{Header:"Computed",columns:[{Header:"Plugins Executed",id:"plugins",accessor:function(e){return e},Cell:function(e){var t=e.value;return Object(m.jsxs)("div",{className:"d-flex flex-column align-items-start",children:[Object(m.jsxs)("span",{children:[t.analyzers_to_execute.length,"/",t.analyzers_requested.length||"all"," analyzers"]}),Object(m.jsxs)("span",{children:[t.connectors_to_execute.length,"/",t.connectors_requested.length||"all"," connectors"]})]})},disableSortBy:!0,maxWidth:175},{Header:"Process Time (s)",id:"process_time",accessor:"process_time",disableSortBy:!0,maxWidth:125},{Header:"Status",id:"status",accessor:"status",Cell:function(e){var t=e.value;return Object(m.jsx)(b.c,{status:t})},disableSortBy:!0,Filter:l.C,selectOptions:j.b,minWidth:225}]}],tableEmptyNode:Object(m.jsxs)(m.Fragment,{children:[Object(m.jsx)("h4",{children:"No Data"}),Object(m.jsx)("small",{className:"text-muted",children:"Note: Try changing time filter."})]})};function v(){console.debug("JobsTable rendered!"),c()("IntelOwl | Jobs History",{restoreOnUnmount:!0});var e=Object(l.S)(),t=e.range,a=e.fromTimeIsoStr,s=e.onTimeIntervalChange,d=Object(l.R)({url:o.q,params:{received_request_time__gte:a},initialParams:{ordering:"-received_request_time"}},f),u=Object(n.a)(d,3),b=u[0],j=u[1],v=u[2];return Object(m.jsxs)(r.a,{fluid:!0,children:[Object(m.jsxs)(i.a,{className:"d-flex-start-center flex-column flex-lg-row mb-2",children:[Object(m.jsxs)("h1",{children:["Jobs History\xa0",Object(m.jsxs)("small",{className:"text-muted",children:[null===b||void 0===b?void 0:b.count," total"]})]}),Object(m.jsx)(l.k,{className:"ml-auto",size:"sm",defaultSelected:t,onChange:s})]}),Object(m.jsxs)(i.a,{className:"px-3 bg-dark d-flex justify-content-end align-items-center",children:[Object(m.jsx)(l.H,{}),Object(m.jsx)(l.G,{onClick:v,className:"ml-auto m-0 py-1"})]}),Object(m.jsx)(i.a,{children:j})]})}}}]);