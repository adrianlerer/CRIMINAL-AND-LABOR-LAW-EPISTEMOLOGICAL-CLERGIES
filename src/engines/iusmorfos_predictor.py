"""
Iusmorfos Predictor

Predicts legal transplant success (WEIRD vs No-WEIRD contexts).

Iusmorfos analyzes institutional and cultural factors to predict whether
legal concepts will successfully transplant across different contexts.
"""

import numpy as np
import pandas as pd
from typing import Dict, List, Optional, Tuple
import logging

from code.bootstrap import BootstrapValidator

logger = logging.getLogger(__name__)


class IusmorfosPredictor:
    """
    Predictor for legal transplant success.
    
    Analyzes:
    - WEIRD (Western, Educated, Industrialized, Rich, Democratic) contexts
    - No-WEIRD contexts
    - Institutional compatibility
    - Cultural distance
    """
    
    def __init__(self, db=None, n_bootstrap: int = 1000):
        """
        Initialize Iusmorfos predictor.
        
        Parameters:
        -----------
        db : Database connection
            Connection to institutional/cultural database
        n_bootstrap : int
            Bootstrap iterations for validation
        """
        self.db = db
        self.validator = BootstrapValidator(n_iterations=n_bootstrap)
        
        # WEIRD dimension weights (placeholder)
        self.weird_dimensions = {
            'wealth_index': 0.2,
            'education_index': 0.2,
            'industrialization': 0.15,
            'democracy_index': 0.25,
            'rule_of_law': 0.2
        }
        
        logger.info("IusmorfosPredictor initialized")
    
    def classify_jurisdiction(
        self,
        jurisdiction: str
    ) -> Dict:
        """
        Classify jurisdiction as WEIRD or No-WEIRD.
        
        TODO: Implement with actual institutional data.
        
        Parameters:
        -----------
        jurisdiction : str
            Jurisdiction name
            
        Returns:
        --------
        dict : Classification with confidence scores
        """
        # PLACEHOLDER
        logger.warning("Using placeholder jurisdiction classification.")
        
        # Simulate WEIRD score
        weird_score = np.random.uniform(0, 1)
        
        return {
            'jurisdiction': jurisdiction,
            'weird_score': weird_score,
            'classification': 'WEIRD' if weird_score >= 0.5 else 'NO_WEIRD',
            'dimensions': {
                'wealth': np.random.uniform(0, 1),
                'education': np.random.uniform(0, 1),
                'industrialization': np.random.uniform(0, 1),
                'democracy': np.random.uniform(0, 1),
                'rule_of_law': np.random.uniform(0, 1)
            }
        }
    
    def predict_transplant_success(
        self,
        concept_name: str,
        source_jurisdiction: str,
        target_jurisdiction: str
    ) -> Dict:
        """
        Predict success probability of legal transplant.
        
        Uses institutional compatibility and cultural distance.
        
        Parameters:
        -----------
        concept_name : str
            Legal concept to transplant
        source_jurisdiction : str
            Origin jurisdiction
        target_jurisdiction : str
            Destination jurisdiction
            
        Returns:
        --------
        dict : Prediction with confidence intervals
        """
        logger.info(f"Predicting transplant: {concept_name} from {source_jurisdiction} to {target_jurisdiction}")
        
        # Classify jurisdictions
        source_class = self.classify_jurisdiction(source_jurisdiction)
        target_class = self.classify_jurisdiction(target_jurisdiction)
        
        # Calculate institutional distance
        institutional_distance = self._calculate_institutional_distance(
            source_class['dimensions'],
            target_class['dimensions']
        )
        
        # Calculate cultural compatibility
        cultural_compatibility = self._calculate_cultural_compatibility(
            source_jurisdiction,
            target_jurisdiction
        )
        
        # Predict success probability
        # Simple model: success = f(institutional_similarity, cultural_compatibility)
        success_prob = (
            0.5 * (1 - institutional_distance) +
            0.5 * cultural_compatibility
        )
        
        # Bootstrap validation
        # Simulate prediction uncertainty
        bootstrap_samples = np.random.beta(
            success_prob * 10 + 1,
            (1 - success_prob) * 10 + 1,
            self.validator.n_iterations
        )
        
        ci_lower, ci_upper = self.validator.calculate_bootstrap_ci(bootstrap_samples, 0.95)
        
        results = {
            'concept': concept_name,
            'source': source_jurisdiction,
            'target': target_jurisdiction,
            'source_classification': source_class['classification'],
            'target_classification': target_class['classification'],
            'success_probability': float(success_prob),
            'ci_95': (float(ci_lower), float(ci_upper)),
            'ci_lower': float(ci_lower),
            'ci_upper': float(ci_upper),
            'institutional_distance': float(institutional_distance),
            'cultural_compatibility': float(cultural_compatibility),
            'recommendation': self._generate_recommendation(success_prob),
            'risk_factors': self._identify_risk_factors(
                source_class, target_class, institutional_distance, cultural_compatibility
            )
        }
        
        logger.info(f"Predicted success: {success_prob:.2%}, CI: [{ci_lower:.2%}, {ci_upper:.2%}]")
        
        return results
    
    def _calculate_institutional_distance(
        self,
        source_dims: Dict[str, float],
        target_dims: Dict[str, float]
    ) -> float:
        """
        Calculate institutional distance between jurisdictions.
        
        Parameters:
        -----------
        source_dims : dict
            Source jurisdiction dimensions
        target_dims : dict
            Target jurisdiction dimensions
            
        Returns:
        --------
        float : Distance [0, 1]
        """
        distances = []
        for key in source_dims:
            if key in target_dims:
                distances.append(abs(source_dims[key] - target_dims[key]))
        
        return float(np.mean(distances)) if distances else 0.5
    
    def _calculate_cultural_compatibility(
        self,
        source_jurisdiction: str,
        target_jurisdiction: str
    ) -> float:
        """
        Calculate cultural compatibility score.
        
        TODO: Implement with actual cultural data.
        
        Parameters:
        -----------
        source_jurisdiction : str
        target_jurisdiction : str
            
        Returns:
        --------
        float : Compatibility [0, 1]
        """
        # PLACEHOLDER
        # In real implementation, would use:
        # - Language similarity
        # - Legal family proximity
        # - Historical connections
        # - Trade relationships
        
        return float(np.random.uniform(0.4, 0.9))
    
    def _generate_recommendation(self, success_prob: float) -> str:
        """
        Generate transplant recommendation based on success probability.
        
        Parameters:
        -----------
        success_prob : float
            Predicted success probability
            
        Returns:
        --------
        str : Recommendation text
        """
        if success_prob >= 0.8:
            return "HIGHLY RECOMMENDED: High probability of successful adaptation"
        elif success_prob >= 0.6:
            return "RECOMMENDED: Good probability with careful implementation"
        elif success_prob >= 0.4:
            return "CAUTION: Moderate probability, requires significant adaptation"
        else:
            return "NOT RECOMMENDED: Low probability without major modifications"
    
    def _identify_risk_factors(
        self,
        source_class: Dict,
        target_class: Dict,
        institutional_distance: float,
        cultural_compatibility: float
    ) -> List[str]:
        """
        Identify potential risk factors for transplant.
        
        Parameters:
        -----------
        source_class : dict
            Source jurisdiction classification
        target_class : dict
            Target jurisdiction classification
        institutional_distance : float
            Institutional distance
        cultural_compatibility : float
            Cultural compatibility
            
        Returns:
        --------
        list : Risk factors
        """
        risks = []
        
        # WEIRD mismatch risk
        if source_class['classification'] != target_class['classification']:
            risks.append(f"WEIRD/NO-WEIRD mismatch: Concept originates in {source_class['classification']} context")
        
        # High institutional distance
        if institutional_distance > 0.5:
            risks.append(f"High institutional distance ({institutional_distance:.2f})")
        
        # Low cultural compatibility
        if cultural_compatibility < 0.5:
            risks.append(f"Low cultural compatibility ({cultural_compatibility:.2f})")
        
        # Specific dimension warnings
        for dim, source_val in source_class['dimensions'].items():
            target_val = target_class['dimensions'].get(dim, 0.5)
            if abs(source_val - target_val) > 0.6:
                risks.append(f"Large {dim} gap: {abs(source_val - target_val):.2f}")
        
        return risks if risks else ["No major risk factors identified"]
    
    def compare_multiple_targets(
        self,
        concept_name: str,
        source_jurisdiction: str,
        target_jurisdictions: List[str]
    ) -> pd.DataFrame:
        """
        Compare transplant success across multiple target jurisdictions.
        
        Parameters:
        -----------
        concept_name : str
            Legal concept
        source_jurisdiction : str
            Source jurisdiction
        target_jurisdictions : list
            List of potential target jurisdictions
            
        Returns:
        --------
        pd.DataFrame : Comparison table
        """
        logger.info(f"Comparing {len(target_jurisdictions)} potential transplant targets")
        
        results = []
        for target in target_jurisdictions:
            prediction = self.predict_transplant_success(
                concept_name,
                source_jurisdiction,
                target
            )
            results.append({
                'target_jurisdiction': target,
                'success_probability': prediction['success_probability'],
                'ci_lower': prediction['ci_lower'],
                'ci_upper': prediction['ci_upper'],
                'classification': prediction['target_classification'],
                'institutional_distance': prediction['institutional_distance'],
                'recommendation': prediction['recommendation']
            })
        
        df = pd.DataFrame(results)
        df = df.sort_values('success_probability', ascending=False)
        
        return df
    
    def generate_prediction_report(
        self,
        concept_name: str,
        source_jurisdiction: str,
        target_jurisdiction: str
    ) -> str:
        """
        Generate comprehensive transplant prediction report.
        
        Parameters:
        -----------
        concept_name : str
        source_jurisdiction : str
        target_jurisdiction : str
            
        Returns:
        --------
        str : Formatted report
        """
        prediction = self.predict_transplant_success(
            concept_name,
            source_jurisdiction,
            target_jurisdiction
        )
        
        report = []
        report.append("=" * 60)
        report.append("IUSMORFOS TRANSPLANT PREDICTION REPORT")
        report.append("=" * 60)
        report.append("")
        report.append(f"Concept: {concept_name}")
        report.append(f"Source: {source_jurisdiction} ({prediction['source_classification']})")
        report.append(f"Target: {target_jurisdiction} ({prediction['target_classification']})")
        report.append("")
        report.append("SUCCESS PREDICTION:")
        report.append(f"  Probability: {prediction['success_probability']:.1%}")
        report.append(f"  95% CI: [{prediction['ci_lower']:.1%}, {prediction['ci_upper']:.1%}]")
        report.append(f"  Recommendation: {prediction['recommendation']}")
        report.append("")
        report.append("COMPATIBILITY METRICS:")
        report.append(f"  Institutional distance: {prediction['institutional_distance']:.3f}")
        report.append(f"  Cultural compatibility: {prediction['cultural_compatibility']:.3f}")
        report.append("")
        report.append("RISK FACTORS:")
        for risk in prediction['risk_factors']:
            report.append(f"  ⚠ {risk}")
        report.append("")
        report.append("=" * 60)
        
        return "\n".join(report)


# Standalone function for batch predictions
def predict_batch_transplants(
    transplant_pairs: List[Tuple[str, str, str]],
    n_bootstrap: int = 1000
) -> pd.DataFrame:
    """
    Predict transplant success for multiple concept-source-target triples.
    
    Parameters:
    -----------
    transplant_pairs : list of tuples
        List of (concept, source_jurisdiction, target_jurisdiction)
    n_bootstrap : int
        Bootstrap iterations
        
    Returns:
    --------
    pd.DataFrame : Batch predictions
    """
    predictor = IusmorfosPredictor(n_bootstrap=n_bootstrap)
    
    results = []
    for concept, source, target in transplant_pairs:
        prediction = predictor.predict_transplant_success(concept, source, target)
        results.append(prediction)
    
    return pd.DataFrame(results)
