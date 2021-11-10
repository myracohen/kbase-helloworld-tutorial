/*
A KBase module: myracohen_HellowWorld
*/

module myracohen_HellowWorld {
    typedef structure {
        string report_name;
        string report_ref;
    } ReportResults;

    /*
        This example function accepts any number of parameters and returns results in a KBaseReport
    */
    funcdef run_myracohen_HellowWorld(mapping<string,UnspecifiedObject> params) returns (ReportResults output) authentication required;

};
