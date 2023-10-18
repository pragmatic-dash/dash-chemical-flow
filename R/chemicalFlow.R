# AUTO GENERATED FILE - DO NOT EDIT

#' @export
chemicalFlow <- function(id=NULL, edges=NULL, height=NULL, label=NULL, nodes=NULL, selectionEvent=NULL) {
    
    props <- list(id=id, edges=edges, height=height, label=label, nodes=nodes, selectionEvent=selectionEvent)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'ChemicalFlow',
        namespace = 'dash_chemical_flow',
        propNames = c('id', 'edges', 'height', 'label', 'nodes', 'selectionEvent'),
        package = 'dashChemicalFlow'
        )

    structure(component, class = c('dash_component', 'list'))
}
