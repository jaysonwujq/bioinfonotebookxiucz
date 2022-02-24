```
\documentclass[a4paper]{article}
\usepackage{microtype}
\usepackage[margin=2.54cm]{geometry}
\usepackage{graphicx,booktabs,tabularx}
\usepackage[table]{xcolor}

\newcolumntype{R}{>{\leavevmode\color{magenta!70!black}\ignorespaces\sffamily\bfseries}p{2.5cm}}%
\newcolumntype{H}{>{\leavevmode\color{orange!30!black}\ignorespaces\raggedright\arraybackslash\sffamily}X}%
\newcolumntype{J}{>{\leavevmode\color{green!30!black}\ignorespaces\sffamily}X}%
\newcolumntype{W}{>{\leavevmode\color{blue!30!black}\ignorespaces\raggedleft\arraybackslash\sffamily}X}%

\rowcolors{2}{purple!05}{olive!05}
\begin{document}
\centering
{\resizebox*{\textwidth}{\textheight}{%
\renewcommand{\arraystretch}{2}
\begin{tabularx}{\textwidth}{RHJW}
\toprule\rowcolor{white}
    & \textbf{Hibernate OGM} & \textbf{EclipseLink NoSQL} & \textbf{DataNucleus}\\\midrule
  Goal & Complement JPA with NoSQL, key-value stores & Integrates in the father project main goal of providing a complete persistence solution & Being a standards compliant and efficient JPA and JDO platform\\
  NoSQL and Datastores supported & Infinispan, EHCache, MongoDB & MongoDB, Oracle NoSQL, Oracle AQ, JMS, XML files & Google Big Table, MongoDB, Cassandra, Excel, OOXML, ODF, XML, HBase, AppEngine/DataStore, Neo4j, JSON, Amazon S3, GoogleStorage, LDAP, NeoDatis, db4o\\
  Operations supported & Object Oriented queries (JP-QL), CRUD of entities, Polymorphic entities, Embeddable objects, Basic types (partial), Unidirectional and Bidirectional relationships (partial), Collections, Hibernate Search queries, JPA and Hibernate ORM API & Object Oriented Queries, Polymorphic entities, Basic types, Unidirectional relationships, Collections, JPA (partial), Complex hierarchical, Indexed hierarchical data, Mapped hierarchical data, CRUD operations, Embedded objects and collections, Inheritance, Subset of JP-QL and Criteria API, Denormalization & CRUD operations, Embedded objects and collections, Inheritance, Relationships (Unidirectional and Bidirectional), Queries for JP-QL, JDOQL and SQL (partial),  Basic types, Joins.\\
  No support for & Denormalization, Complex joins and aggregations & Joins & Aggregations? (not specified in documentation)\\
  Future & High performance sequence generator, parallel key fetching, support for Map/Reduce, more NoSQL classes, better mixing of NoSQL and RDBMS & ? & JPA2.1 full feature list, Official support for Cassandra, Considering a plugin for REDIS\\
  Commercial support & Red Hat & Oracle (via TopLink) & Supported by DataNucleus team\\
  Documentation & Scattered, inactive forums, official documentation lacking & Bureaucratic forums, information is complete and gathered mainly in the official website & Active forums, acceptable official documentation, but the big advantage comes from user support in form of blogs and posts scattered around the Internet\\\bottomrule
\end{tabularx}}}
\end{document}
```