package LeetCode;

import java.util.*;

class AccountsMerge {

    class DSU {
        int[] parent;
        public DSU() {
            parent = new int[10001];
            for (int i = 0; i <= 10000; ++i)
                parent[i] = i;
        }
        public int find(int x) {
            if (parent[x] != x) parent[x] = find(parent[x]);
            return parent[x];
        }
        public void union(int x, int y) {
            parent[find(x)] = find(y);
        }
    }

    public List<List<String>> accountsMerge(List<List<String>> accounts) {
        DSU dsu = new DSU();
        Map<String, String> emailToName = new HashMap(); // maps emails to the account name
        Map<String, Integer> emailToID = new HashMap(); // maps emails to an id
        int id = 0;
        for (List<String> account: accounts) {
            String name = "";
            for (String email: account) {
                if (name == "") {
                    name = email;
                    continue;
                }
                emailToName.put(email, name);
                if (!emailToID.containsKey(email)) {
                    emailToID.put(email, id++);
                }
                dsu.union(emailToID.get(account.get(1)), emailToID.get(email)); // union the first email with the email we are at in the account
            }
        }

        Map<Integer, List<String>> ans = new HashMap();
        for (String email: emailToName.keySet()) {
            int index = dsu.find(emailToID.get(email));
            ans.computeIfAbsent(index, x-> new ArrayList()).add(email); //group the sets of emails into a sortable list
        }
        for (List<String> component: ans.values()) {
            Collections.sort(component); // sort each set
            component.add(0, emailToName.get(component.get(0))); //add the account name to the zero'th position
        }
        return new ArrayList(ans.values());
    }
}
