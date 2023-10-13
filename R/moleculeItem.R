# AUTO GENERATED FILE - DO NOT EDIT

#' @export
moleculeItem <- function(value=NULL) {
    
    props <- list(value=value)
    if (length(props) > 0) {
        props <- props[!vapply(props, is.null, logical(1))]
    }
    component <- list(
        props = props,
        type = 'MoleculeItemReact',
        namespace = 'dash_chemical_flow',
        propNames = c('value'),
        package = 'ChemicalFlow'
        )

    structure(component, class = c('dash_component', 'list'))
}
