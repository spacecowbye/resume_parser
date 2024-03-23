def get_work_experience_resume(resume):
    ''' prompt to find the work experience from the resume '''

    work_experience = """
   sample_resume_text =" EDUCATION
ColumbiaUniversity NewYork,NY
MasterofScienceinDataScience,GPA:4.08/4.00 Dec2020
Coursework:MachineLearning,AppliedMachineLearning,AppliedDeepLearning,StatisticalInference&Modeling,
PersonalizationTheory,NaturalLanguageProcessing,AlgorithmsforDataScience,ComputerSystems,ExploratoryData
AnalysisandVisualization
NirmaUniversity Ahmedabad,India
BachelorofTechnologyinComputerEngineering,GPA:9.50/10,Rank:2/900 May2019
Coursework:MachineLearning,DeepLearning,ArtificialIntelligence,LinearAlgebra,Algorithms
WORK EXPERIENCE
SLBSoftwareTechnologyInnovationCenter(STIC) MenloPark,CA
DataScientist Feb2021-Present
Physics-InformedMachineLearningandTimeSeriesAnalysis
● DevelopedPhysicsInformedMachineLearningbasedHybridFrameworktocreateanadvisorysystemthatidentifiesthe
regionswithriskyStick/Slipconditionsandoutputsanoptimaloperatingwindowfordrillingthefuturestands
● DevisedHybridframeworkusingPhysicsInformedMachineLearningfordigitallygeneratingLWDlogs(Gamma-Ray
logs)inreal-timetoincreaseefficiencyandrobustnessoflogcollectionprocess
● WorkingtowardsimplementationofPhysicsInspiredMachineLearningbasedtoolboxforTimeSeriesdata
ComputerVision
● ResearchedandimplementedvariousComputerVisionbasedusecasestoimproveHealthSafetyandEnvironment
● Evaluated5+stateoftheatsolutionsforObjectDetection,ObjectTracking,andPoseEstimation.Fine-tuneddifferent
objectdetectionmodelsandintegratedthemintotheposeestimationpipelinesforincreasedperformanceforfielddatasets
MediaCenterofArtandHistoryatColumbiaUniversity NewYork,NY
GraduateResearchAssistant Mar2020-Dec2020
● Engineeredwaytoautomateprocessofslideanalysisforcollectionofslides,deployingimageprocessingandML/DL
techniquestodetectoriginalityofphotographicimagesin35mmslidescollection
● Formulatedpipelinetoreplicateentiremanualprocessbyinitiallyfilteringimagesbasedoncitationusedinslides,followed
byidentifyingpresenceofHalftonepatterns(Precision:95%,Recall:82%)
Unilever EnglewoodCliffs,NJ
DataScienceAnalyst Mar2020-Dec2020
● DevelopedanddeployedanapplicationtostreamlinethefeatureextractionanddataengineeringprocessforProcess
AnalyticsEngine
● SupporteddevelopmentofProcessAnalyticsEnginetogettheinsightsinteractivelyusingthedatacollectedfrom
productionunit
1
SwissReinsuranceAmericaCorporation Armonk,NY
DataScientistIntern May2020-Aug2020
● DesignedanddevelopedSmartUnderwritingFrameworktogeneratescoresforeachsubmissionbasedonpropensityto
bind;PrioritizingprocessingforsubmissionsbasedonscoresimprovedCumulativeGainsby20%
● AnalyzedDriftinDatausingKLDivergenceandLogisticRegression-basedmodels,constructedtechniquetoretrain
modeldynamicallyinproductionsettingtoensureDomainAdaptability
● Researchedvariouspapers,articles,anddatasetsavailableforIndividualHealthForecasting;Reviewtaskresultedin
documentsummarizing89researchpapersinvolvingDL-basedapproachesforElectronicHealthRecords
SamsungR&DInstitute Noida,India
ResearchIntern Jan2019-May2019
● ResearchedvariousOn-DeviceAIsolutionsaspartofAIcoreteamandcontributedtoenhancingqualityofservices
providedbySamsungforitsmobiledevices;ProducedML/DLmodelsbyutilizingScikit-learn,TensorFlow,TF-Lite
frameworks
● DevisedtechniquesforFacialAnti-SpoofingSystemleveragingvariousML/DLmethodsinPythonanddeployeditasan
AndroidApplication
● AnalyzeddifferentOn-DeviceAIsolutionsforhealthandmultimediaservicesonlow-endSamsungsmartphoneswith
1GBofRAMtoensurerobustnessofsolutions
PUBLICATIONS
JournalPublications:
[1]ParamPopat,PrashamSheth,andSwatiJain."Animal/ObjectIdentificationUsingDeepLearningonRaspberryPi."In
InformationandCommunicationTechnologyforIntelligentSystems:ProceedingsofICTIS2018,Volume1,pp.319-327.
SpringerSingapore,2019.
[2]PrashamSheth,PriyankThakkar,andPraxalPatel."OptimalLocationPredictionforEmergencyStationsUsingMachine
Learning."InternationalJournalofOperationalResearch.2022.
[3]PrashamSheth,SaiShravaniSistla,IndranilRoychoudhury,MengdiGao,CrispinChatar,JoseCelaya,andPriyaMishra.
"Real-TimeGammaRayLogGenerationfromDrillingParametersofOffsetWellsUsingPhysics-InformedMachine
Learning."SPEJournal(2023):1-11.
ConferencePublications:
[1]PrashamSheth,IndranilRoychoudhury,CrispinChatar,andJoséCelaya."AHybridPhysics-BasedandMachine-Learning
ApproachforStick/SlipPrediction."In IADC/SPEInternationalDrillingConferenceandExhibition.OnePetro,2022.
[2]PrashamSheth,SaiShravaniSistla,IndranilRoychoudhury,MengdiGao,CrispinChatar,JoseCelaya,andPriyaMishra.
"Real-TimeDigitalLogGenerationfromDrillingParametersofOffsetWellsUsingPhysicsInformedMachineLearning."
In SPE/IADCInternationalDrillingConferenceandExhibition.OnePetro,2023.
ACADEMIC PROJECTS
EnergyEfficientAIonEdgeDevices(MasterThesisProject) Sep2020-Dec2020
● DevelopedtechniquesforcompressingDeepLearningModelsforfasterinferenceonedgedevicesandreducedcarbon
footprintinassociationwithGEResearch
● ResearchedPost-trainingquantization,QuantizationAwareTraining(QAT),andmodelPruningtechniquesformodel
compressing
● Designedlowlatencycompressedmodelswithminimalaccuracydropforformulatedmodelsformultipledatasets
HybridapproachcombiningContentandModel-basedTechniquesforRecommendation Sep2019-Dec2019
● CreatedRestaurantRecommendationSystembasedonYelpdataset(2019)(6,685,900reviews,192,609businesses,200,000
pictures,tenmetropolitanareas,over1.2millionbusinessattributes:hours,parking,availability,andambiance)
● DevelopedRecommendationSystemutilizingvarioustechniques:AlternatingLeastSquarebasedMatrixFactorization,
FactorizationMachines,Content-basedRecommendationcapturinginformationfromImages/Text-basedreviews
2
● AcceleratedperformanceofRecommendationEnginebyengineeringwaytocombineresultsfromvariousapproachesto
cultivatestrengthsofeachmodelandgetmoregeneralizedrecommendations
OptimalLocationPredictionforEmergencyStations Jul2018-Jan2019
● Identifiedandengineeredvariousinfluencingparametersnamelylocationattributes,populationdensity,traffic,navigation,
frequencyofambulancecalls,andweatherconditions
● FormulatedvariousML/DLModelstoidentifybestsuitableforTravelTimeEstimationbetweendifferentlocationsofcity;
TravelTimeestimatedfromXGBoostisusedtodriveK-Medoidsforpredictingoptimallocations
● Conceptualizedapproachdemonstratedpromisingtestresults-Decreasedturnaroundtimealongwithreducedutilityof
resources;forStatenIsland:averagetimereducedby6secondsutilizing14FireStationsincomparisonto19actualones
End-to-EndSentenceLevelLipreading Jan2018-Apr2018
● Designedmodelforperformingend-to-endsentencelevellip-reading,ratherthanapproachesofdetectingindividualwords
bysimultaneouslyrecognizingspatiotemporalvisualfeaturesandsequencemodel;Improvedperformancebyapproximately
10%overtheLSTMBaseline
● Structuredmethodtoprocessframes(capturedat25fpsfromGRIDCorpus)leveragingcombinationofCNNand
BidirectionalGatedRecurrentUnits(Bi-GRUs)toenhanceperformanceofend-to-endsentenceformation
SKILLS
● ProgrammingLanguages:Python,SQL,R,Java,C++,C
● ToolsandTechnologies:Scikit-Learn,NumPy,Pandas,Statsmodels,PyTorch,OpenCV,Scipy,GoogleBigQuery,Oracle
DS,MongoDB,GoogleCloudPlatform,GitHub,LaTeX
"

    sample output = 
    
        "Job Title": "Data Scientist",
        "Company": "SLB Software Technology Innovation Center (STIC)",
        "Start Date": "Feb2021",
        "End Date": "Present"
    
    
        "Job Title": "Graduate Research Assistant",
        "Company": "Media Center of Art and History at Columbia University",
        "Start Date": "Mar2020",
        "End Date": "Dec2020"
    
    
        "Job Title": "Data Science Analyst",
        "Company": "Unilever",
        "Start Date": "Mar2020",
        "End Date": "Dec2020"
    
    
        "Job Title": "Data Scientist Intern",
        "Company": "Swiss Reinsurance America Corporation",
        "Start Date": "May2020",
        "End Date": "Aug2020"
    
]   
from the resume_text provided figure out all the job history of the candidate and return it in the form of sample output, do not write anything else no clarification needed.

    If not found return N/A
do not return any other text, just the job title,company,start date,end date, no need for further clarifications

    """
    
    return  resume + '\n' + work_experience


def get_skills_resume(resume):
    ''' prompt to find the list of skills from the resume '''

    skills = """
    1. what are the skills of the candidate. Please make a list of the skills mentioned in the JD
    the answer should be return in this format 
    skills :


    
    if you are unabale to find the skills then return NA"""
    
    return skills + '\n' + resume


def get_education_resume(resume):
    ''' prompt to find the education from the resume '''


    education = """
    1. what are the education degree of the candidate. Please make a list of the Job description mentioned in the JD
    the answer should be return in this format. 
    educations : degree name


    
    if you are unabale to find the skills then return NA"""
    
    return education + '\n' + resume


def get_recent_title_resume(resume):
    ''' prompt to find the recent position from the resume '''


    title = """ 1. what is the current position of the candidate in his latest company
    the answer should be return in this format. 
    position : position name

    
    if you are unabale to find the skills then return NA"""
    
    return title + '\n' + resume


def get_recent_location_resume(resume):
    ''' prompt to find the location from the resume '''

    location = """ 1. what is the most recent location of the candidate in his latest company
    the answer should be return in this format. 
    location : location name

    
    if you are unabale to find the skills then return NA"""
    
    return location + '\n' + resume

def calculate_work_ex(st):
    ''' method to calculate the total work exp of candidate from the string '''


    total = 0
    for ex in st.split('\n'):
        if 'year' in ex:
            total += int( ex.split(':')[-1].strip() )
        if 'month' in ex:
            total += float( ex.split(':')[-1].strip() ) /12
    
    return total


def get_min_education_resume (resume):
    ''' prompt to find the education from the resume '''

    education_resume = """Please fetch the following details from the Job description
    1. what are the education degree mention in the resume below, Please return the list of degrees
    the answer should be in format
    education : 
    """
    return education_resume + '\n' + resume